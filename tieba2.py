#-*- coding: utf-8 -*-
import urllib2,re

tiezi = raw_input('请输入帖子地址：')
def geturl(i):
    url =tiezi+'?see_lz=1'+'&pn='+str(i)                  #只看楼主模式
    req = urllib2.urlopen(url).read().decode('utf-8')
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
    pat2 = re.compile(r'id="post_content.*?>(.*?)</div>')    #最最普通的文本，其他较特殊 的情况还需要根据实际情况另外写正则
    txt = pat2.findall(req,re.S)
    return txt
 
tempreq = geturl(1)   
number = getpagenumber(tempreq)[0]
print number
title = gettitle(tempreq)
f = open(title+'.txt','w')
for i in range(int(number)+1):
    req = geturl(i)
    txt = getcontent(req)
    for eachitem in txt:
        f.write(eachitem.replace('<br>',''))
        f.write('\n')
f.close()



