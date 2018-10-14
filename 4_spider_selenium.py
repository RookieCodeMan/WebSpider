# 总结一下，主要是利用selenium库来获取动态渲染的页面， 直接模拟浏览器来实现爬取
# 再使用selenium webdriver之前需要提前安装好chromedriver
# 将chromedriver.exe复制到script的安装目录下，并配置好环境变量
# 将chrome的安装目录添加到环境变量中
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def selenium_demno():
    browser = webdriver.Chrome()
    try:
        browser.get("https://www.taobao.com")
        print(browser.page_source)
        input = browser.find_element_by_id('kw')
        input.send_keys('Python')
        input.send_keys(Keys.ENTER)
        wait = WebDriverWait(browser, 10)
        wait.until(EC.presence_of_all_elements_located((By.ID, 'content_left')))
    finally:
        browser.close()


def find_element():
    browser = webdriver.Chrome()
    try:
        browser.get("https://www.taobao.com")
        # print(browser.page_source)
        input_first = browser.find_element_by_id('q')
        input_second = browser.find_element_by_css_selector('#q')
        # 在css selector支持id、class定位
        # "#"代表id, "."代表class
        print(input_first, input_second)
    finally:
        browser.close()


def find_elements():
    browser = webdriver.Chrome()
    try:
        browser.get("https://www.taobao.com")
        lst = browser.find_elements_by_css_selector('.service-bd li')
        print(lst)
    finally:
        browser.close()


def send_keys():
    browser = webdriver.Chrome()
    try:
        browser.get("https://www.taobao.com")
        input = browser.find_element_by_id('q')
        input.send_keys('iPhone')
        time.sleep(1)
        input.clear()
        input.send_keys('ipad')
        button = browser.find_element_by_class_name('btn-search')
        button.click()

    finally:
        browser.close()


if __name__ == '__main__':
    # find_elements()
    send_keys()
