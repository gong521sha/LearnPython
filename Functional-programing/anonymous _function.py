# -*- coding: utf-8 -*-
f = lambda x: x % 2 == 1
print(f(1))#匿名函数无法写显示的return返回值，它返回的是表达式的值，比如x % 2 == 1，返回的就是True或者False

print(f(1,2))

#请用匿名函数改造下面的代码
def is_odd(n):
    return n % 2 == 1

L1 = list(filter(is_odd, range(1, 20)))

L2 = list(filter(lambda x: x% 2 == 1,range(1,20)))

print(L1,L2)