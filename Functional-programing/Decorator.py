# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 13:21:26 2018

@author: sha521gong
"""


'''
装饰器指的是在代码运行期间动态增加功能的方式，而不修改原函数的定义。简单来说，可以把装饰器理解为一个包装函数的函数，它一般将传入的函数
或者是类做一定的处理，返回修改之后的对象。所以我们能够在不修改原函数的基础上，在原函数之行前后执行别的代码，比较常用的场景有日志插入，事务处理等。
'''
#我们定义一个函数，foo()
def foo():
    print('foo')
    
#我有一个需求，我想知道这个函数是否被调用过，需要知道调用日志，如果调用了就打印一串字符，我们可以如下的改造
def foo():
    print('foo')
    print('foo is running')
    
#如果每个函数都需要记录日志，那么需要对每个函数进行改造，这是不能接受的。我们可以重新定义一个函数，专门处理日志，日志处理完之后再执行真正的业务代码
def logging(func):#传入的参数是一个函数
    print("%s is running" % func.__name__)#利用函数内置的__name__属性来获取函数的名字
    func()#同时执行原函数
#原函数不变，但增加了日志打印功能，同时具有通用性，每个函数都可以使用。 
    
def foo():
    print('foo')
logging(foo)

'''
上述函数逻辑好理解，但是每次都要将一个函数作为参数传递给logging函数。而且这种方式破坏了原有的代码逻辑结构，以前执行业务时，
运行foo()皆可，但现在要改成logging(foo)，有没有更好的方式，答案是有的，那就是装饰器。
'''
def decorator_logging(func):
    def wrapper(*args,**kwargs):
        print("%s is running" % func.__name__)
        return func(*args,**kwargs)
    return wrapper
def foo():
    print('foo')
  
decorator_foo = decorator_logging(foo)#装饰器返回增强版原函数的一个引用
decorator_foo()
'''
函数decorator_logging()就是装饰器，它把执行真正业务方法的func包裹在函数里，看起来像foo被decorator_logging装饰了。
这里面还有一个概念，就是函数进入和退出时，被称为一个横切面（Aspect），这种变成方式被称为面向切面的变成（Aspect-Oriented Programming）
'''
#上面的例子还不是很完美，因为还存在decorator_foo = decorator_logging(foo)语句，我们可以采用语法糖的方式让代码更加简洁
def decorator_logging(func):
    def wrapper(*args,**kwargs):
        print("%s is running" % func.__name__)
        return func(*args,**kwargs)
    return wrapper

@decorator_logging
def foo():
    print('foo')

foo()

#如果我们想让其他函数实现这个打印功能，同样可以使用这个装饰器,比如
@decorator_logging
def helloWorld():
    print('hello World!')
helloWorld()


#带参数的装饰器例如比如decorator_logging(x),这种方式增加了装饰器编写和使用的灵活性。

def decorator_logging(level):
    def decorator(func):
        def wrapper(*args,**kwargs):
            if level=='warn':
                print("%s is running" % func.__name__)
            return func(*args,**kwargs)
        return wrapper
    return decorator
#foo = decorator_logging('warn')(foo)
#foo()
@decorator_logging(level='warn')
def foo():
    print('foo')

foo()

'''
上面的等效于foo = decorator_logging('warn')(foo),我们来剖析上面的语句，首先执行decorator_logging('warn')，返回的
是decorator函数，再调用返回的函数，参数是foo函数，返回值最终是wrapper函数。
这里面有一个问题，就是经过decorator装饰之后的函数，他们的__name__已经从原来的'foo'变成了'wrapper'
'''
foo = decorator_logging('warn')(foo)
print(foo.__name__)
#打印出来的函数名字是wrapper，因为返回的函数名字就是wrapper，所以需要把原始函数的__name__等属性复制到wrapper函数中，否则
#有些依赖函数签名的代码执行就会出错，此时可以使用python内置的functools.wraps，一个完整的decorator的写法如下：
import functools
def decorator_logging(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator
'''
这里解决最后一个问题，就是wrapper()函数为什么要使用*args, **kwargs作为参数，假如上面的例子中foo()函数是有参数的，那么wrapper()
就必须要带相对应个数的参数，那么通用性就无法实现了。我们知道*args表示可变参数，**kwargs表示关键字参数，所有函数的参数都可以表示成这种形式。
所以wrapper(*args, **kw)是适配了所有函数的参数类型
'''    











































