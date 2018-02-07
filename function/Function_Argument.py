# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 14:41:07 2018

@author: gong521sha
"""
#默认参数
#n就是默认参数,默认参数设置原则是函数有n个参数，如果第m（m<n）个参数是设置为了默认参数，那么m之后的参数都必须为默认参数。函数也可以全部都设置默认参数
#如果默认参数后面是非默认参数，编译器会抛出 non-default argument follows default argument错误
def power(x,n=2): 
    d = 1
    while n>0:
        n = n -1
        d = d * x
    return d
print(power(5,4))
#ps:定义默认参数要牢记一点：默认参数必须指向不变对象！ 默认参数n的默认值是2，但不代表n就只能是数字，它可以是字符串，可以是list，可以是dict

#可变参数，顾名思义，可变参数就是传入的参数个数是可变的，可以是1个、2个到任意个，还可以是0个
def calc(*numbers): #看出什么不同来了吗？那就是在参数前面加上*就变成了可变参数
    #print(len(numbers))
    sum = 0
    for n in numbers:
        sum = sum + n
    return sum

#可变参数*numbers实际是一个tuple，它将输入的多个值变成一个元组，传入函数中。当然输入的值也可以是list或者tuple
l=[1,2,3]
print(calc(*l)) # *t表示传入的是一个可变参数
t=(4,5,6)
print(calc(*t))
print(calc(*t,*l)) #传入的是t和l两个变量，从输出结果来看，*number将两个变量合成了一个那就是（1,2,3,4,5,6）

#关键字参数
#可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。而关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict
def person(name, age, **kw): #person()这个函数的位置参数是2个，而不是3个
    print('name:', name, 'age:', age, 'other:', kw)
person('hello',20)
person('hello',20,city=65)

person_plus = {'city':'beijing','weight':80,'edu':'master'}
person('hello',20,**person_plus)

#限制关键字参数的命名,和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数。
def person(name, age, *, city, job):#限制了关键参数的明明，key值只能为city和job
    print(name, age, city, job)
person('sandy',18,city='beijing',job='IT')
person_plus = {'city':'beijing','weight':80,'edu':'master'}
person('hello',20,**person_plus)#函数运行被抛出的异常是 person() got an unexpected keyword argument 'weight'

def person2(name, age, *, city, job):
    print(name, age, city, job)
person_plus = {'city':'beijing','job':'IT'}
person2('hello',20,**person_plus)

def person2(name, age, *, city, job):
    print(name, age, city, job)
person_plus = {'name':'sandy','age':18,'city':'beijing','job':'IT'}#从上面的两个例子看出来，python函数关键字的使用非常灵活，可以把所有参数打包成一个dict进行输入
person2(**person_plus)

#限制关键字参数的另外一种写法
def person(name,age,*args,city,job):#如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了
    print(name,age,args,city,job)
person_plus = {'name':'sandy','age':18,'city':'beijing','job':'IT'}
person2(*person_plus)#如果调用时不加**，那么编译器将认为这是一种可变参数的调用，dict里面的内容都将被当成位置参数，就会报错，如下：TypeError: person2() takes 2 positional arguments but 4 were given


#参数组合
#在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
def f1(a, b, c=0,*args,**kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)
f1(1,2,3,{'d':9},ext=7)
#我们可以思考为什么要遵循这种顺序？
#1.默认参数、可变参数和关键字参数必须在必选参数之后，这是因为如果这积累参数在必选参数之后，那么输入多个参数时编译器不知道赋值顺序
#2.关键字参数为什么要在可变参数的后面呢，如果放在前面会引起什么问题？实际和上述的是同样的原因，可变参数可以是普通单个数字，字符串，list，tuple，同样也可以是dict。
#如果将可变参数放在关键字参数之后，那么输入关键字参数时将无法判断输入的是**kw的值还是 *args的值，下面的调用可以解释


#习题练习

#以下函数允许计算两个数的乘积，请稍加改造，变成可接收一个或多个数并计算乘积：
def product(x, y):
    return x * y

#函数改造
def product(*args):
    p=1
    for j in args:
        p=p*j
    print(p)
product(5,6,8)
