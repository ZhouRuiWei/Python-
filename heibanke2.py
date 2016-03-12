# -*- coding: utf-8 -*-
import requests
import sys
url = 'http://www.heibanke.com/lesson/crawler_ex01/'
for i in range(1,31):
    print'trying', i
    dat = {'username':'abc','password':i}
    r =requests.post(url,data=dat)
    if '请重新输入' not in r.text:
        print 'the code is：', i
        break
