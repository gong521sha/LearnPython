# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 14:47:26 2018

@author: sha521gong
map/reduce
"""

"""
map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数一次作用到序列的每个元素，并把结果作为新的Iterator返回
"""

#函数返回一个变量的平方
def f(x):
    return x*x
#利用列表生成式生成一个列表
l = [i+1 for i in range(10)]
#打印mao中的序列
for n in map(f,l):
    print(n)

#reduce是把一个函数作用在一个序列[x1,x2,x3,...]上，这个函数必须接受两个参数，reduce把结果继续喝序列的下一个元素做累计计算，其效果就是
reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)

#对一个序列求和，可以用reduce实现
from functools import reduce
def add(x,y):
    return x+y
l = [i+1 for i in range(10)]
r =reduce(add,l)

"""
利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。
输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：
"""
def firstUppercase(str):
    str2=""
    for i in range(len(str)):
        if i==0:
            str2=str[0].upper()
        else:
            str2=str2+str[i].lower()
    return str2
print(firstUppercase('adam'))
m = map(firstUppercase,['adam', 'LISA', 'barT'])
list(m)

#上面的代码很复杂，有没有更简洁的语法
def firstUppercase(str):
    return str[0].upper()+str[1:].lower()
print(firstUppercase('adam'))
m = map(firstUppercase,['adam', 'LISA', 'barT'])
list(m)

#请写一个prod()函数，可以接受一个list并利用reduce()求积
def prod(x,y):
    print(x,y)
    return x*y
r =reduce(prod,[3,5,7,9])


#字符串转整数，追求代码的简洁和逻辑性
from functools import reduce

CHAR_TO_INT = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9
}

def str2int(s):
    ints = map(lambda ch: CHAR_TO_INT[ch], s)
    return reduce(lambda x, y: x * 10 + y, ints)

print(str2int('0'))
print(str2int('12300'))
print(str2int('0012345'))


#字符串转浮点数
#代码写成横行不如写成竖行的形式
CHAR_TO_FLOAT = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '.': -1#这个设置真是聪明，自愧不如啊。
}

def str2float(s):
    nums = map(lambda ch: CHAR_TO_FLOAT[ch], s)
    point = 0
    def to_float(f, n):
        nonlocal point
        if n == -1:
            point = 1
            return f
        if point == 0:
            return f * 10 + n
        else:
            point = point * 10
            return f + n / point
    return reduce(to_float, nums, 0.0)

print(str2float('0'))
print(str2float('123.456'))
print(str2float('123.45600'))
print(str2float('0.1234'))
print(str2float('.1234'))
print(str2float('120.0034'))


