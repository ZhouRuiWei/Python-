# -*- coding: utf-8 -*-

#a small script to rename files automatically

import os
import os.path
while True:
    dr = raw_input('please input the path of your files:')
    if os.path.isdir(dr): 
        break
    else:
        print 'path not exist,please try again!'
if dr:
    os.chdir(dr)            #改变工作目录到用户输入的文件路径下
    cwd = os.getcwd()        #取得当前工作目录
    files = os.listdir(cwd)  #得到当前工作目录下的所有文件
    print '****files in current path****'
    for file in files:
        print file
    print '*****************************'
    print 'there are %d files'  %len(files)
#输入新名字或者把已有的变量作为新名字
#while True:
#    newname=list(raw_input('please input new names(seperated by space):'))
#    if len(newname)==len(files):
#        break
#    else:
#        print 'wrong number of newnames'




i = 0
for file in files:
    namext = os.path.splitext(files[i])
    extension =namext[1]
    print extension
    os.rename(file,newname[i]+extension)
    i+=1
