#�ڰ������
import requests
import re

# ��һ����ַ
Q1 = r'http://www.heibanke.com/lesson/crawler_ex00/'

url = Q1
num_re = re.compile(r'<h3>[^\d<]*?(\d+)[^\d<]*?</h3')
while True:
    print'���ڶ�ȡ��ַ:',url
    html = requests.get(url).text
    num = num_re.findall(html)
    if len(num) == 0:
        break
    else:
        url = Q1 + num[0]
print('������')
