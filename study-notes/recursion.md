# 函数的递归解析

递归指的是一个计算过程，如果其中每一步都要用到前一步或前几步的结果，成为递归。用递归过程定义的函数成为递归函数

递归函数指的是函数直接或间接调用函数本身。现实生活中有很多案列可用递归的方式实现，比如阶乘、连加、连乘等等，还有一些稍微复杂的递归，比如下面要介绍的汉诺塔和斐波那契数列。

##汉诺塔

汉诺塔(Tower of hanoi)：有三根柱子，其中一根柱子上从下往上按照大小顺序摞着N片圆盘，如何能把这些圆盘移动到灵一根柱子上，规定时间小圆盘上不能放大圆盘，并且在三根柱子之间一次只能移动一个圆盘。

汉诺塔游戏是用来讲解递归函数非常经典的案例，递归就是讲一个大的问题层层转化为一个与原问题相似的规模较小的问题来求解，递归策略只需少量的程序就可描述出解题过程所需要的所需要的多次重复计算，大大减少了程序的代码量，它的能力在于用有限的语句来定义对象的无限集合。一般来说地柜需要有边界条件、递归前进段和递归返回段，当边界条件不满足时，递归前进，当边界条件满足时，递归返回。

汉诺塔问题解析：

> 有A，B，C三根柱子，圆盘在A柱上，我们要将圆盘从A柱移动到C柱：
>
> 1. 1个圆盘
>
> > 我们直接将A柱的圆盘移动到C柱就完成，移动一次 A->C
>
> 2. 2个圆盘
>
> > 我们将A柱圆盘移动到B A->B，再将A柱剩下的圆盘移动到C柱 A->C，然后将B柱的圆盘移动到C B->C
>
> 3. 3个圆盘
>
> > 我们将A柱圆盘移动到C A->C，再将A柱剩下的圆盘移动到B柱 A->B，将C柱圆盘移动到B C->B，将A柱最后一个盘子移动到C A->C，此时A柱圆盘为空，B柱上有两个圆盘，C柱上有1个圆盘，**此时的问题变成了将B柱上的两个圆盘移动到C柱**。
>
> 4. n个圆盘
>
> > 我们可以把这个大的目标先分解成小的目标：
> >
> > + 将n-1圆盘移动到B柱上 A~n-1~ ->B
> > + 将剩下的1个圆盘从A柱移动到C柱 A->C
> > + 将B柱上的n-1个圆盘移动到C柱 B~n-1~->C
> >
> > 这三个步骤就能把任务进行完整的表述，根据这个思路，用代码进行描述

```python
#函数定义
def hanoi(n,a,b,c):
    if n==1:
        print(a,'->',c)#如果只有一个盘子，那么直接从A移动到C
        return 'done'#边界条件，只剩下最后一步操作，那么就结束了
    else:
        hanoi(n-1,a,c,b)#将A柱上的n-1个盘子移动到B柱
        hanoi(1,a,b,c)#将剩下的1个圆盘从A柱移动到C柱
        hanoi(n-1,b,a,c)

#函数执行
hanoi(3,'A','B','C')
```

## 斐波那契数列

*斐波那契数列*又称为*黄金分割数列*，以数学家斐波那契以兔子繁殖为例而引入，故又称为*兔子数列*，数据的具体表示是`1,1,2,3,5,6,13,21,34,.....`

斐波那契的递归表达为：f(0)=0,f(1)=1,f(n)=f(n-1)+f(n-2) (n>=2,n$\in​$N)





# 总结

递归函数的编写还是要找到将复杂问题分解成简单问题的方法与规律