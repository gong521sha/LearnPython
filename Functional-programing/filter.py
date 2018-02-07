# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 16:25:50 2018

@author: sha521gong
filter 过滤器
filter和map()类似，filter()也接收一个函数和一个序列。
和map()不同的是，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。
用filter实现一个筛选的功能
"""

def not_empty(s):
    return s and s.strip()#s and s.strip()是逻辑与的关系，如果s==s.strip()则返回True，如果s!=s.strip()则返回false

list(filter(not_empty, ['A', '', 'B', None, 'C', '  ']))
# 结果: ['A', 'B', 'C']


def main():
    for n in primes():
        if n < 1000:
            print(n)
        else:
            break

#实现一个奇数的构造器,因为偶数不可能是素数
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n

def _not_divisible(n):
    return lambda x: x% n > 0
    #这个lamda是一个三元表达式，相当于
    #def mod(x):
    #    return x%n >0

def primes():
    yield 2#2 也是一个素数，用yield的方式将其抛出
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n), it)

if __name__ == '__main__':
    main()

    
    
    