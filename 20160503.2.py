#-*- coding:utf-8 -*-


# 给出 n 个字符串，对于每个 n 个排列 p，按排列给出的顺序(p[0] , p[1] … p[n-1])依次连接这 n 个字符串都能得到一个长度为这些字符串长度之和的字符串。
# 所以按照这个方法一共可以生成 n! 个字符串。
# 一个字符串的权值等于把这个字符串循环左移 i 次后得到的字符串仍和原字符串全等的数量，
#i 的取值为 [1 , 字符串长度]。
# 求这些字符串最后生成的 n! 个字符串中权值为 K 的有多少个。
# 注：定义把一个串循环左移 1 次等价于把这个串的第一个字符移动到最后一个字符的后面。
# 输入描述:
# 每组测试用例仅包含一组数据，每组数据第一行为两个正整数 n, K ， n 的大小不超过 8 ， K 不超过 200。
# 接下来有 n 行，每行一个长度不超过 20 且仅包含大写字母的字符串。
# 输出描述:
# 输出一个整数代表权值为 K 的字符串数量。
# 输入例子:
# 3 2
# AB
# RAAB
# RA
# 输出例子:
# 3

import itertools

number = raw_input('')
n = int(number.split()[0])
k = int(number.split()[1])

def quanzhi(str):     #计算权值
	K = 1
	length = len(str)
	for i in range(length-1):
		temp = str[i+1:]+str[0:i+1]   #左移i位的字符
		if temp==str:
		    K = K +1
	return K

str = [0 for i in range(n)]
for i in range(n):
	str[i] = raw_input('')

temp = list(itertools.permutations(str,n))   #字符串全排列
allstr = [''.join(x) for x in temp ]         #将字符串连接起来

answer = 0
for x in allstr:
	if quanzhi(x)==k:
		answer+=1


print answer