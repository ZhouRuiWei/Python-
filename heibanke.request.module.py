#黑板课爬虫
import requests
import re

# 第一题网址
Q1 = r'http://www.heibanke.com/lesson/crawler_ex00/'

url = Q1
num_re = re.compile(r'<h3>[^\d<]*?(\d+)[^\d<]*?</h3')
while True:
    print'正在读取网址:',url
    html = requests.get(url).text
    num = num_re.findall(html)
    if len(num) == 0:
        break
    else:
        url = Q1 + num[0]
print('结束！')
