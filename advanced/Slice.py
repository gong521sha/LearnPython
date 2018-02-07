# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 11:33:44 2018
此文件用来描述python的切片功能
@author: gong521sha
"""


#定义一个list
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
#如果想从list中取出部分值
#取某几个元素
s=[]
s.append[L[x]]
#取2-4个元素（n<m）

L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
s=[]
n=2
m=4
x=2-1
while x<=m-1:
    s.append(L[x])
    x=x+1
print(s)

#使用切片方法
L[n:m]#从索引n开始取数，直到m-1，取出的元素个数为m-n
L[0:3]#表示取L[0],L[1],L[2]三个数,如果从索引0开始取的话，可以省略0，L[:3]
#python支持负数索引，比如L[-1]表示最后一个元素
L[-3:]#表示从倒数第三个数取到最后一个

l = list(range(100))
[0, 1, 2, 3, ..., 99]
l[:10]#取前10个数
l[-10:]#取后10个数
l[4:10]#取l[4]--l[9]
L[:10:2]#前是个数，每两个取一个
L[::5]#每5个取一个

#字符串'xxx'也可以看成是一种list，每个元素就是一个字符。因此，字符串也可以用切片操作，只是操作结果仍是字符串：
'ABCDEFG'[:3]
'ABCDEFG'[::2]

#练习
#利用切片操作，实现一个trim()函数，去除字符串首尾的空格，注意不要调用str的strip()方法：
s=' asdf '
def trim(s):
    if s[0].isspace():
        s=s[1:-1]
    elif s[-1].isspace():
        s=s[:-2]
    print(s)
    return s
def trim2(s):
    if s[0]==' ':
        s=s[1:-1]
    elif s[-1]==' ':
        s=s[:-2]
    print(s)
    return s
trim2(s)

