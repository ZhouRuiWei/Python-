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

#获取扩展名
extension=[]
i = 0
for file in files:
    namext = os.path.splitext(files[i])
    extension.append(namext[1])
    i+=1
	

def userinput():   #让用户从键盘输入新名字的模式

    #输入新名字
    newnames = []
    i = 0
    while i<len(files):
        onename=raw_input('please input new names of file '+str(i+1)+':')+extension[i]
        if onename in newnames or onename in files[(i+1):]:                                                                                                                                                           
            print 'name already exist! please input another name'
            continue
        newnames.append(onename)
        i+=1



    #重命名
    print'******newnames*******'
    for i in range(len(files)):
        os.rename(files[i],newnames[i])
        print newnames[i]


		
def series():
    name = raw_input('please enter half of the name without number')
    print'******newnames*******'
    for i in range(len(files)):
        os.rename(files[i],name+str(i+1)+extension[i])
        print name+str(i+1)+extension[i]

		
		
		
		
		
print'''now,if you like to input every newname,please enter 1;
if you like to rename the files with names like file1,file2...please enter 2'''
choice = raw_input('your choice:')
choices={1:userinput,2:series}
choices[int(choice)]()
