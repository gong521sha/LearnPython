# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 14:30:24 2018
迭代
@author: gong521sha
"""

d = {'a': 1, 'b': 2, 'c': 3}

#打印dict的key值
for key in d:
    print(key)

#打印value的值 
for value in d.values():
    print(value)
    
#打印每个key-value
for l,v in d.items():
    print(l,v)
    

#练习
#请使用迭代查找一个list中最小和最大值，并返回一个tuple.练习里面的代码没有考虑一些特殊情况，比如输入参数的判断，数组长度的判断。
L=[2,12,4,53,3,6,78,312,1,2234,3]
def findMinAndMax(L):
    min=L[0]
    max=L[0]
    for i in L:
        if i>=max:
            max=i
        elif i<=min:
            min=i
    return (min, max)
print(findMinAndMax(L))

#enumerate把list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身
for i ,value in enumerate(['A','B','C']):
    print(i,value)