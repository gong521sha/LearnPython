# python函数的参数

python函数参数具有较强的灵活性，首先编译器本身并不检查参数的类型，所以python的函数参数并不用像java一样声明参数类型，并且具有参数数量可变等诸多特点，总结一下python有以下五种类型的参数：

1. 位置参数
2. 默认参数
3. 可变参数 `*args`
4. 关键字参数`**kw`
5. 命名关键字参数



1. 位置参数

```python
def person(name,age):#name和age就属于位置参数，位置参数是必须传进去的参数
```

2. 默认参数

```python
def person(name,age=18):#age就是默认参数，默认参数指的是如果参数传递时不指定数值，则使用默认数值
person('max')#不给age赋值，那么age传递的就是默认参数
person('max',20)#给age赋值为20
```

3. 可变参数

```python
def person(name,age=18,*args)#可变参数顾名思义就是参数是可变的，*args表示声明了一个可变参数，这个参数可以由多个参数组成。实质上是多个参数组装成了一个tuple或者list被传递进去.
#eg.
person('max',20,'beijing','make',180)#可以直接传递三个变量进去，这三个变量直接被组装成了一个list传递了进去，等同于下面的语句
L = ['beijing','male',180] #声明了一个list，有三个变量
person('max',20,*L)
```

4. 关键字参数

```python
def person(name,age=18,**kw)#**kw就是关键字参数，它传递的参数形式就是key=value的形式，也就是说传递的多个key-value会被自动组装成dict
person('max',20,city='beijing',sex='male')#这种方式等同于下面的例子
d = {'city':'beijing','sex'='male'}
person('max',20,**d)
```

*args和**kw只是一个约定俗成的写法，你也可以写成别的，但最好按照习惯来写。

5. 命名关键字参数

```python
def person(name,age=18,*,city,sex)#命名关键字参数指的是传递时只接受指定为city和sex的关键字参数。命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数.如果不加这个*，那么编译器会认为是4个位置参数
peson('max',20,city='beijing',sex='male')
```

