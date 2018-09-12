import requests
import re
import json
from requests.exceptions import RequestException


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
    # 解析html文件，正则表达式
    # re.S的作用，表示将.的作用扩展到整个字符串
    # api带flag的都可以带上re.S表示正则.的作用范围为整个字符串
    regex = '<dd>.*?board-index.*?>(.*?)</i>.*?data-src="(.*?)".*?name.*?a.*?>(.*?)</a>.*?star.*?>(.*?)</p>' \
            '.*?releasetime.*?>(.*?)</p>.*?score.*?integer.*?>(.*?)</i>.*?fraction.*?>(.*?)</i>'
    parse_results = re.findall(regex, html, re.S)
    print(parse_results)
    for result in parse_results:
        yield {
            "rank": result[0],
            "image": result[1],
            "name": result[2],
            "star": result[3].strip()[3:],
            "release_time": result[4].strip()[5:],
            "score": result[5].strip() + result[6].strip()
        }


def write_to_file(content):
    with open("file_100.txt", 'a', encoding='utf-8') as file:
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
