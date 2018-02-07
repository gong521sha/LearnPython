# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 12:10:20 2018

@author: sha521gong
生成器
"""

"""
通过列表生成式，我们可以直接创建一个列表。但是，受到内存限制，列表容量肯定是有限的。
而且，创建一个包含100万个元素的列表，不仅占用很大的存储空间，如果我们仅仅需要访问前面几个元素，那后面绝大多数元素占用的空间都白白浪费了。
所以，如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素呢？
这样就不必创建完整的list，从而节省大量的空间。在Python中，这种一边循环一边计算的机制，称为生成器：generator。
"""

g = (x*x for x in range(10))
#generator保存的是算法，通过调用next(g)来计算下一个元素的值，直到计算到最后一个元素，然后抛出StopIteration
for i in g:
    print(i)

t=[]
def fib(max):
    n,a,b=0,0,1
    while n<max:
        print(b)
        a,b=b,a+b#python语言的语法非常的灵活，这个赋值语句相当于t=[a,a+b] a=t[0],b=t[1]
        #上面的赋值语句可以进行下面的改造
#        t=[b,a+b]
#        a=t[0]
#        b=t[1]
        n+=1
    return "done"
fib(10)

#将上面的函数变化成generator，生成器的执行顺序是每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return "done"

for n in fib(9):#这个fib的返回值是b，也就是yield后面的数值，而不是return后面的值
    print(n)
    
"""
          1
         / \
        1   1
       / \ / \
      1   2   1
     / \ / \ / \
    1   3   3   1
   / \ / \ / \ / \
  1   4   6   4   1
 / \ / \ / \ / \ / \
1   5   10  10  5   1
"""
#用generator实现杨辉三角
#整个函数实现的思路就是先确定前两行的list，分别为l[1],l[1,1],然后利用这两个list去构造新的list
def triangles():
    L=[1]
    while True:
        yield L
        L=[1]+[L[i]+L[i+1] for i in range(len(L)-1)]+[1]
        
t=triangles()
for n in range(5):
    print(next(t))



