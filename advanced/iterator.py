# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 14:16:03 2018

@author: sha521gong
迭代器:iterator
"""

"""
我们知道，可以直接作用于for循环的数据类型有以下几种：
一类是集合数据类型，如list、tuple、dict、set、str等；
一类是generator，包括生成器和带yield的generator function。
这些可以直接作用于for循环的对象统称为可迭代对象：Iterable
可以使用isinstance()判断一个对象是否是Iterable对象
"""
from collections import Iterable
isinstance([], Iterable)#前面是需要判断的对象，后面是判断的对象的类型

#generator不但可以作用于for循环，还可以被next()函数不断调用并返回下一个值，直到最后抛出StopIteration错误表示无法继续返回下一个值。
#可以被next函数不断调用并返回下一个值的对象成为迭代器：Iterator