# -*- coding:utf-8 -*-


# 在一个二维数组中，每一行都按照从左到右递增的顺序排序，
# 每一列都按照从上到下递增的顺序排序。
# 请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
# 输入描述:
# array： 待查找的二维数组
# target：查找的数字
# 输出描述:
# 查找到返回true，查找不到返回false


class Solution:
    # array 二维列表
    def Find(self, array, target):
        # write code here
        n = len(array)-1
        i = 0
        while True:
            if len(array[0])==0:
                return False
                break
            if n<0 or  i>=len(array[0]):
                return False
                break
            if array[n][i] == target:
                return True
                break
            if array[n][i]<target:
                i+=1
            else:
                n-=1
            
