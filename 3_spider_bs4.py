import requests
import re
import json
from requests.exceptions import RequestException
from bs4 import BeautifulSoup


def get_one_page(url):
    # 这边如果不加headers 反爬虫会检查到，提示恶意访问
    try:
        headers = {
            "User-Agent": 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                          ' Chrome/69.0.3497.92 Safari/537.36'}
        response = requests.get(url, headers=headers)
        # 区分response.text和response.content
        # content返回的是bytes类型，用于传输文件，图片等
        # text返回的是unicode类型，用于传输文本
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None


def parse_one_page(html):
    # 解析html文件，用beautiful解析库来替代正则表达式
    # beautiful在解析的时候，依赖解析器,lxml解析器可以解析HTML和XML
    soup = BeautifulSoup(html,'lxml')
    # 节点选择器，字节点也可以选择，只会选择第一个匹配到的节点,后面的节点会被忽略
    # 方法选择器，find_all,用find_all查找dd的节点，返回的是一个list
    dd_elements = soup.find_all(name='dd')
    for dd_element in dd_elements:
        img_elements = dd_element.find_all(name='img')
        p_elements = dd_element.find_all(name='p')
        i_elements = p_elements[3].find_all(name='i')
        yield {
            "rank": dd_element.i.string,
            "image": img_elements[1].attrs['data-src'],
            "name": p_elements[0].string,
            "star": p_elements[1].string.strip()[3:],
            "release_time": p_elements[2].string,
            "score": i_elements[0].string.strip() + i_elements[1].string.strip()
        }


def write_to_file(content):
    with open("file_100_bs4.txt", 'a', encoding='utf-8') as file:
        # 如果直接写，报错，write的参数必须是str类型
        # ensure_ascii确保了输出结果是中文，而不不是unicode编码
        file.write(json.dumps(content, ensure_ascii=False) + '\n')


def main(offset):
    url = 'http://maoyan.com/board/4?offset=' + str(offset)
    html = get_one_page(url)
    for content in parse_one_page(html):
        write_to_file(content)


if __name__ == '__main__':
    for i in range(10):
        main(i*10)
