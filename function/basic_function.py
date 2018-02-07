# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 11:31:59 2018

@author: gong521sha
"""

#python的编译器参数并不检查参数的类型，如果想检查参数类型，只能通过代码验证参数类型，如果不符合，则抛出异常。
#python可以返回多个值，但编译器会自动将多个参数封装成一个tuple，多个变量可以接收同一个tuple值，并根据顺序赋予每个变量对应的值。
#函数可以没有返回值，在函数执行到最后没有使用return语句时，自动return none

#定义一个求绝对值的函数
def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x

#如果想定义一个什么事也不做的空函数，可以用pass语句
def null_function():
    pass


#pass还可以用在其他语句里，比如：
age=20
if age >= 18:
    pass #if语句后必须要跟具体操作，但是如果不知道具体操作是什么，可以使用pass
    
    
#测试返回值
def return_value_number():
    return 1,2
a,b = return_value_number()


#practis
#请定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程：ax2 + bx + c = 0的两个解。计算平方根可以调用math.sqrt()函数
import math
def quadratic(a, b, c):
    mid = math.sqrt(b*b-4*a*c)
    return -(b/2*a)+mid/2*a,-(b/2*a)-mid/2*a
print(quadratic(1,-2,1))
