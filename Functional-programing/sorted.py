# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 09:59:05 2018

@author: gong521sha
"""

l = [1,3,5,8,-2]
sorted(l)#默认将数值从小到达排列

def absolute(i):
    if i<0:
        return -i
    else:
        return i
sorted(l,key=absolute)#sorted函数本身也是一个高阶函数，可以接受其他函数


name = ['gong','Yan','sha']
sorted(name)#默认对于字母按照ASCII码的方式进行排序
sorted(name,key=str.lower)#改变key的值，以小写方式进行排序

#假设我们用一组tuple表示学生名字和成绩,请用sorted()对上述列表分别按名字排序
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
print(sorted(L))#通过结果可以看出，sorted对于二元数组默认是通过第一个元素进行排序

def by_name(t):
    return t[0]
print('通过名字进行排序：',sorted(L,key=by_name))
def by_score(t):
    return t[1]
print('通过分数进行排序：',sorted(L,key=by_score))


'''
count()函数返回的是一个list，list里面的每一个元素是一个函数。
'''
def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs

f1 = count()
for i in f1:
    print(i())
#为什么三个函数都返回9，而不是，1，4，9.那是因为返回的函数引用了变量i，但它并非立刻执行。等到3个函数都返回时，它们所引用的变量i已经变成了3，因此最终结果为9。
    
#练习，利用闭包返回一个计数器函数，每次调用它返回递增整数
def createCounter():
    i = 0
    def counter():
        nonlocal i#nonlocal表明i变量是函数的外层变量
        i = i + 1
        return i
    return counter
counterA= createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA())


#通过下面这个例子来加强理解python函数变量的作用域

def add_b():
    #global  b
    b = 42#这里的b是add_b()中的局部变量
    def do_global():
        global  b#要注意的是这里的b和前面的b并不是同一个变量,这里的b是全局变量b
        b =  10
        print("b = %s " % b)
    do_global()
    b  = b + 5#这里的b是函数内的局部变量b
    print("b = %s " % b)
add_b()
b = b + 30
print("b = %s " % b)























