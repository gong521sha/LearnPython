# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 11:30:37 2018

@author: gong521sha
"""

#递归函数recursive function
#下面的函数用来求一个数的阶乘
def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)
print(fact(100))

#上面的递归函数和下面的循环函数是等价的
def fact2(n):
    if n==1:
        return 1
    j=1
    p=1
    while j<n+1:
        p=p*j
        j=j+1
    return p
print(fact2(100))


#使用递归函数的优点是逻辑简单清晰，缺点是过深的调用会导致栈溢出。
#针对尾递归优化的语言可以通过尾递归防止栈溢出。尾递归事实上和循环是等价的，没有循环语句的编程语言只能通过尾递归实现循环。
#Python标准的解释器没有针对尾递归做优化，任何递归函数都存在栈溢出的问题。

#递归函数练习
#汉诺塔的移动
#汉诺塔：汉诺塔（又称河内塔）问题是源于印度一个古老传说的益智玩具。
#大梵天创造世界的时候做了三根金刚石柱子，在一根柱子上从下往上按照大小顺序摞着64片黄金圆盘。大梵天命令婆罗门把圆盘从下面开始按大小顺序重新摆放在另一根柱子上。并且规定，在小圆盘上不能放大圆盘，在三根柱子之间一次只能移动一个圆盘。
mn=0
def move(n,a,b,c):
    if n<=0 or (not isinstance(n,int)):
        raise TypeError('参数必须为正且为整数')
    elif n==1:
        print(a,'-->',c)
    else:
        mn=mn+1
        move(n-1,a,c,b) #子目标1：将a柱的n-1个盘移动到b柱上
        move(1,a,b,c) #子目标2：将a柱的最后一个盘移动到c柱上
        move(n-1,b,a,c) #子目标3：将b柱的盘移动到c柱上
move(2,'A','B','C')
print(move_numvber)
#递归函数的应用就在于把问题抽象化，找到其中的规律，也就是把大的目标转化成小的可循环的子目标。
