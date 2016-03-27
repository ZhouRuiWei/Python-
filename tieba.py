# -*- coding: utf-8 -*-

import string, urllib2,os
#-------- 输入起止页面的页码 ------------------
#贴吧地址例如http://tieba.baidu.com/f?kw=公路车&ie=utf-8&pn=0
url = str(raw_input(u'请输入贴吧的地址:'))[:-1]
begin_page = int(raw_input(u'请输入开始的页数：\n'))
end_page = int(raw_input(u'请输入终点的页数：\n'))
#--------开始读取并且保存网页--------------
for i in range(begin_page, end_page+1):
    filename = 'page  '+str(i) + '.html'         
    print 'downloading' + str(i) + 'html,and name it as' + filename + '......'
    f = open(filename,'w+')
    m = urllib2.urlopen(url + str(i)).read()
    f.write(m)
    f.close()
print 'finish,files are in '+os.getcwd()
 
 
