#-*- coding: utf-8 -*-

import urllib,re,os
from bs4 import BeautifulSoup

tiezi = raw_input('请输入帖子地址：')
def geturl(i):
    url =tiezi+'?see_lz=1'+'&pn='+str(i)
    req = urllib.urlopen(url).read().decode('utf-8')
    return req

def getpagenumber(req):
    pat3 = re.compile(r'<span class="red">(\d*)</span>')
    number = pat3.findall(req)
    return number

def gettitle(req):
    pat1 = re.compile(r'<title>(.*?)</title>')
    longtitle =pat1.findall(req)[0].split('_')
    title = '-'.join(longtitle[:-2])
    return title

	
def getcontent(req):
    soup = BeautifulSoup(req)
    contents = soup.findAll("div",{"id":re.compile("post_content.*")})
    return contents
 
tempreq = geturl(1)   
number = getpagenumber(tempreq)[0]
print u"楼主一共发布了"+number+u"页的帖子"
title = gettitle(tempreq)
f = open(title+'.txt','w')
for i in range(int(number)):
    print u"正在读取第"+str(i+1)+"页的内容"
    req = geturl(i+1)
    txt = getcontent(req)
    for eachitem in txt:
        f.write(eachitem.get_text())
        f.write("\n")
f.close()
print u"已经保存到本地"+os.getcwd()



