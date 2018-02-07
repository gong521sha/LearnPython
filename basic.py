#variable $ datatype
int1=1 #integer
hex_int2=0x998 #hexadecimal integer
f1=0.012 #float
f2=1.2e-2 #float scientific notation
str1 = "hello world" #string
str2 = "hello \"world" #string ESC(escape character)
b1 = True #boole "True False" capitalize the first letter
b2 = True and True #"and" "or" "not" opeartor


#List
friends = ['tony','kevin','sandy']
friends[0] #通过索引来访问list中的变量，索引的起始值为0
friends.append('debi') #list是一个可变的有序表，可以通过append命令添加元素到末尾
friends.insert(1,'max') #也可以通过insert命令在指定位置插入元素
friends.pop(1) #使用pop命令删除某个元素
friends = ['python', 'java', ['asp', 'php'], 'scheme'] #list本身可以嵌套

#Tuple
#tuple和数据相似，但是tuple一旦创建就无法修改,这里说的不变指的是tuple已经创建，指向不发生变化
t=(1,2)
t=() #定义了一个空的tuple
t=(1,) #定义了只有一个元素的tuple，这里要注意，只有一个元素，要在元素后面加入一个逗号，否则会被认为是算数运算的括号
t=(1,2,[3,4]) #嵌套了list的tuple，这里面list的值可以改变


#条件判断
a=2
if a>1:
    print("True")
elif a<=2:
    print("False")
else:
    print("Not sure")


#circulation循环,break打断循环退出，continue跳过当前循环
#for循环，for x in ... 把每个元素代入变量x中，然后执行缩进块的语句
sum = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sum = sum + x
print(sum)
   
#上面的公式等价于下面的公式，range（x）表示生成x个整数序列,但是要注意range是从0开始计数
sum = 0
for x in range(10):
    sum = sum + x
    print(x)
print(sum) 
#while循环
n=10
sum=0
while n >0:
    sum=sum+n
    n=n-1
print(sum)
#pracitse
L = ['Bart', 'Lisa', 'Adam']
#方法1：
for name in L:
    print(name)
#方法2：
for x in range(len(L)):
    print(L[x])

#dict
#dict就是字典，通过key-value的方式进行存储
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85} #key就是Michael value就是95
print('sandy' in d)#判断'sandy'是否在d这个字典中

#set set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。
#set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作：
s1 = set([1, 2, 3]) #创建set集合，需要提供一个list
s2 = set([2, 3, 4])
print(s1 & s2) # 两个集合的交集
print(s1 | s2) #两个集合的并集











