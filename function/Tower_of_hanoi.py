#汉诺塔移动
#汉诺塔游戏的规则是三根柱子，其中一个柱子上有从下往上从大到小的N个罗盘，每次移动1个罗盘，其中大罗盘不能放在小罗盘之上，最后把罗盘从A柱移动B柱。
#分别用递归函数或者循环的方式去实现

#使用递归函数去解决，递归函数就是要找到逻辑关系
#1.假设有A，B，C三根柱子，罗盘初始在A柱上，最后有移动到C柱。我们首先要想办法把最下面最大的罗盘移动到C柱上，这个时候B柱上有N-1个罗盘，A柱上没有罗盘，C柱上有一个最大的罗盘。
#2.这个问题此刻又变成了将B柱上的N-1个罗盘移动到C柱，这本身就形成了一种递归。
#综合上面的分解，把汉诺塔拆解成散步，第一步将n-1个盘子移动到B柱上，第二步将A柱上的罗盘移动到C柱上，第三部将n-1个罗盘移动到C柱上
move_count = 0
def hanoi(n,a,b,c):#n表示有n个罗盘
    global move_count#python由于没有变量声明，所以变量的作用于为赋值的区域，如果不加global关键字，那么move_count变量会被认为是函数内变量。
    # 那么move_count = move_count + 1表达式会直接报错"reference before assigment"
    if n==1:
        move_count = move_count + 1
        print(a,'->',c)#如果只有一个罗盘，那就直接从A移动到C
        return 'done'
    else:
        hanoi(n-1,a,c,b)
        hanoi(1,a,b,c)
        hanoi(n-1,b,a,c)
hanoi(3,'A','B','C')
print('移动的次数为：',move_count)

#使用非递归的方式进行实现
