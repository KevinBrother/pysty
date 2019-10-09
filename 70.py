""" import requests
from bs4 import BeautifulSoup

def main():
    resp = requests.get('https://v.taobao.com/v/content/live?catetype=704&from=taonvlang')
    soup = BeautifulSoup(resp.text, 'lxml')
    print('---------soup.select------------', soup.select('img[src]'))
    for img_tag in soup.select('img[src]'):
        print(img_tag.attrs['src']) """


# sudo pip install selenium
# chromeDriver需要翻墙：http://chromedriver.chromium.org/
# http://npm.taobao.org/mirrors/chromedriver/ 国内镜像

# export PATH=$PATH:/home/brother/software/chromedriver/
# 解析动态内容

from bs4 import BeautifulSoup
from selenium import webdriver

def main():
    driver = webdriver.Chrome()
    driver.get('https://v.taobao.com/v/content/live?catetype=704&from=taonvlang')
    soup = BeautifulSoup(driver.page_source, 'lxml')
    print('---------soup.select------------', soup.select('img[src]'))
    for img_tag in soup.select('img[src]'):
        print(img_tag.attrs['src'])

if __name__ == "__main__":
    main()