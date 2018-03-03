[TOC]

# 装饰器的定义

装饰器指的是在代码运行期间不修改原函数定义的情况下动态增加功能的方式。简单来说，可以把装饰器理解为一个包装函数的函数，它将传入的函数或者是类做一定的处理，返回修改之后的对象。装饰器一般用在日志插入、事务处理等场景。

python支持装饰器是因为一切皆对象的设计模式，可以将函数作为另外一个函数的参数。

#装饰器的编写和使用

下面我们将一步一步的讲解装饰器的作用及使用方法

## 普通函数

函数功能非常简单，就是打印一个Hello World！

```python
def hello():
    print('Hello World!')
hello()
```

我现在有一个需求，我想在这个函数被调用时打印一个调用的日志，那我们可以做如下的改造:

```python
def hello():
    print('hello is running')
    print('Hello World!')
hello()
```

##将函数作为参数的函数

上面的改造虽然可以实现业务需求，但是这种改动不具有普适性，就是如果我想知道另外一个函数的调用日志，那么要对其他函数进行改造，这是不能接受的。我们可以重新定义一个函数，接收一个函数作为参数，在处理完日志之后再执行业务代码。

```python
def logging(func):
    print('%s is running' % func.__name__)
    func()
def hello():
    print('Hello World!')
logging(hello)
```

上面的代码存在一个问题，那就无法得到func函数的返回值，所以应该做一定改动，代码如下：

```python
def logging(func):
    print('%s is running' % func.__name__)
    return func()#这种方式是就是在执行了函数的同时可获得函数的返回值
```



上面的方式实现了业务需求，但它改造了原有的调用方式，原有的调用方式为hello(),现在变为logging(hello),有没有一种方式可以在不改变调用方式的情况下实现业务需求，答案就是装饰器

## 不带参数的装饰器

不改变hello()原有的调用方式，就要返回的函数是hello的一个应用，代码如下：

```python
def logging(func):
    def wrapper():
        print('%s is running' % func.__name__)
        return func()
    return wrapper
def hello():
    print('Hello World!')
   
hello = logging(hello)#将hello作为参数传递进logging函数，同时该函数返回wrapper函数的引用
hello()#执行hello()相当于执行了wrapper()
```

上述代码实现打印日志的同时，不改变原函数的定义，同时也不改变原函数的调用方式。为了更加直观和简洁的使用装饰器，python支持语法糖，代码如下

```python
@logging  # @符号后面跟装饰器名字，下面的函数就自动被logging这个装饰器装饰
def hello():
    print('Hello World!')
hello()
```

这里面有一个问题，假如hello()这个函数自身是带参数的，比如

```python
def hello(content):
    print('%s' % content)
```

那么这种情况下上面装饰器的编写方式就会报错，因为func()不带参数，那么采用何种写法既可以装饰带参数的函数也可以装饰不带参数的函数呢，要用到前面学到的可变参数和关键字参数，代码如下

```python
def logging(func):
    def wrapper(*args,**kwargs):#使用可变参数*args和关键字参数**kwargs，就可以支持带参和不带参的函数
        print('%s is running' % func.__name__)
        return func(*args,**kwargs)
    return wrapper
```

## 带参数的函数

我们还可以让装饰器带上参数，带参数的装饰使用更加的灵活

```python
def logging(level):
    def decorator(func):
        def wrapper(*args,**kwargs):
            if level=='warn':
                print("%s is running" % func.__name__)
            return func(*args,**kwargs)
        return wrapper
    return decorator

@logging('warn')
def hello():
    print('Hello World!')
    
hello()
```

## 完整写法的装饰器

上面的带参数的装饰器可以实现功能，但是存在一个问题，函数引用的名字发生了变化

```python
print(hello.__name__)#这个语句打印出来的结果是wrapper，因为返回的函数是wrapper
```

最完美的解决方法是将原始函数的一些属性也复制到wrapper函数中，否则有些依赖函数签名的代码执行就会出错，此时可以使用python内置的functools.wraps，它同样是一个装饰器，一个完整的decorator的写法如下：

```python
import functools
def decorator_logging(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)#这里返回的是函数的执行结果
        return wrapper#这里返回的是wrapper函数的引用
    return decorator
```

