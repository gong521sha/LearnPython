# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 15:12:13 2018
列表生成式
列表生成式即List Comperhensions，是python内置的非常简单却强大的可以用来创建list的生成式
@author: gong521sha
"""

#要生成list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
l = list(range(1,11))

#如果要生成[1x1, 2x2, 3x3, ..., 10x10]怎么做？
l = list(range(1,11))
L=[]
for i in l:
    L.append(i * i)
print(L)

#但是用列表太繁琐，用列表生成式就简单的多
#最前面的 i*i是表达式，for是循环，后面的if是条件
L=[i*i for i in range(1,11)]

#列表生成式后面可以跟判断逻辑,比如只保留可以整除3的数字
L=[i*i for i in range(1,11) if i%3==0]

#可以使用两层循环，形成全排列
L=[m + n for m in 'ABC' for n in 'XYZ']



import os # 导入os模块，模块的概念后面讲到
L=[d for d in os.listdir('.')] # os.listdir可以列出文件和目录,'.'可以列出当前用户默认目录



#练习，将L中的字符变成小写并重新生成一个list
L1 = ['Hello', 'World', 18, 'Apple', None]
L2=[s.lower() if isinstance(s,str) else s for s in L1]#限制性for循环，如果取出的s是字符串则变成小写，else没有变化.
print(L2)

#列表生成式中if else语句有两种形式
#[variable for variable in range() if condition],这里的conditon起判断作用，满足条件的，被返回，不满足条件的被丢弃。
#[variable if condition else conditon for variable in range()],此时if起赋值作用，满足条件的 i 以及 else被用来生成最终的列表
L = [i*i if i%2==0 else 'a' for i in range(1,6)]
#上面的表达式等效于
for i in range(1,6):
    if i%2==0:
        L.append(i*i)
    else:
        L.append('a')
    