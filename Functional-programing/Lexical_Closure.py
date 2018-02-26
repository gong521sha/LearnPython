# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 15:09:57 2018

@author: sha521gong
"""

'''
闭包函数：在一个外函数中定义了一个内函数，内函数里引用了外函数的临时变量，并且外函数的返回值是内函数的引用。
'''
def outer(a):
    def inner(b):
        return a+b
    return inner

c = outer(5)#outer返回inner的引用
print(c(3))#c(3)实质上是inner(3)
print(c(6))

'''
一般的变量随着函数的退出而销毁，但如果外部函数在退出时检测到内部函数引用了外部函数的变量，那么会将此变量绑定到内部函数中，
从而外部函数的变量的生命周期得到了延长
'''

#练习，利用闭包返回一个计数器函数，每次调用它返回递增整数。
#这个练习就是利用闭包的特性。闭包函数每次调用时外部函数的变量并不销毁，而是绑定到内部函数中。
def createCounter():
    i = 0
    def counter():
        nonlocal i 
        i = i + 1
        return i
    return counter

# 测试:
counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')