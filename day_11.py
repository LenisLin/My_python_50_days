## day_11
## 元组（tuple）

# 元组也是多个元素按照一定的顺序构成的序列。元组和列表的不同之处在于，元组是不可变类型，
# 这就意味着元组类型的变量一旦定义，其中的元素不能再添加或删除，而且元素的值也不能进行修改。
# 定义元组通常使用`()`字面量语法

## 定义一个三元组
tuple_1 = (1,2,3) 

## 查看类型
print(type(tuple_1)) 

## 查看元组中元素个数
print(len(tuple_1)) 

## 利用下标索引元组的元素
print(tuple_1[1]) 
print(tuple_1[-1]) # note:负索引就相当于逆向索引了

## 判断成员是否存在于元组
print(1 in tuple_1) 

## 拼接元组
tuple_2=("A",'B','C')
print(tuple_1+tuple_2)

## 元组切片
print(tuple_2[2::]) ## 从下标为2的地方开始切片

## 比较运算（必须相同类型才能比较）
print(tuple_1<(10,20,30))

## 一元组
# `()`表示空元组，但是如果元组中只有一个元素，需要加上一个逗号，否则`()`就不是代表元组的字面量语法，而是改变运算优先级的圆括号
() ## 空元组
(100) ## ()功能为改变运算优先级的()
(100,) ## 一元组

## 元组的应用场景
## eg1:打包和解包
# 把多个用逗号分隔的值赋给一个变量时，多个值会打包成一个元组类型；当我们把一个元组赋值给多个变量时，元组会解包成多个值然后分别赋给对应的变量
# 相当于就是把多个变量暂时用一个元组来进行存放
a = (1,10,100)
i,j,k=a ## i j k三个变量对应a的三个元素
print(i,j,k)
# note：解包出来的元素个数和变量个数不对应，会引发`ValueError`异常

## 一个变量接受多个值：星号（*）表达式，带有星号的变量就会自动变成一个list，如果没有对应值就是空List,如果对应多个值就是多元素的list
i,*j = a
print(i,j)
# note：解包语法中，星号表达式只能出现一次

# 解包语法对所有的序列都成立（包括容器类型的元组、列表和字符串）
## 对range类型
a,b,*c=range(10)
print(a,b,c)
## 对List类型
a,b,c=[1,10,100]
print(a,b,c)
## 对str类型
a,b,*c="hello,world"
print(a,b,c)

## 函数的可变参数
# 前面定义过函数的可变参数，实际上就是在传值的过程中把所有的实际参数打包成元组，传递到函数中
def add(*args):
    print(type(args))
    total=0
    for i in args: ## 利用这种方式可以轻松的遍历，不一定要像C语言那样用下标了
        total += i
    return total

print(add(1,2,3))
print(add(1,3,4,5,6,77,9))

## eg2：交换两个变量的值
# 在C,java里面，交换两个变量的值都需要通过临时变量来实现（交换两杯水）
# Python定义了val1,val2=val2,val1这样的交换方式
a=1
b=2
print(a,b)
a,b=b,a
print(a,b)

## 三个变量也可以
a=1
b=2
c=3
print(a,b,c)
a,b,c=c,a,b
print(a,b,c)

# note：Python的字节码指令中有`ROT_TWO`和`ROT_THREE`这样的指令可以实现两个/三个变量的互换（效率高）

## eg3:函数返回多个值
# 这里其实和定义函数的时候传入多变量类似，这里就是在函数return的时候，把多个结果打包成元组来返回
def find_max_and_min(*args):
    max_=args[0]
    min_=args[0]
    for i in args:
        if(i>max_):
            max_=i
        if(i<min_):
            min_=i
    return max_,min_ ## 这里return两个值，就是打包成一个元组返回
print(type(find_max_and_min(1,2,3,4,5))) ## <class 'tuple'>
print(find_max_and_min(1,2,3,4,5))

## tuple vs. list
# ①元组是不可变类型，**不可变类型更适合多线程环境**，因为它降低了并发访问变量的同步化开销
# ②元组是不可变类型，通常**不可变类型在创建时间和占用空间上面都优于对应的可变类型**
# 我们可以使用`sys`模块的`getsizeof`函数来检查保存相同元素的元组和列表各自占用了多少内存空间。
# 我们也可以使用`timeit`模块的`timeit`函数来看看创建保存相同元素的元组和列表各自花费的时间
import sys
import timeit
a=list(range(1,10000))
print(type(a))

b=tuple(range(1,10000))
print(type(b))

print(sys.getsizeof(a),sys.getsizeof(b))

print(timeit.timeit('[1, 2, 3, 4, 5, 6, 7, 8, 9]'))
print(timeit.timeit('(1, 2, 3, 4, 5, 6, 7, 8, 9)'))
## conclusion：元组的创建时间和占用内存空间都小于列表

## tuple和list的相互转化
a=[1,2,3]
print(a)

a=tuple(a)
print(a)

## 总结
# 列表和元组都是容器型的数据类型，即一个变量可以保存多个数据。
# **列表是可变数据类型**，**元组是不可变数据类型**，所以列表添加元素、删除元素、清空、排序等方法对于元组来说是不成立的。
# 但是列表和元组都可以进行**拼接**、**成员运算**、**索引和切片**这些操作
# 同之前讲到的字符串类型一样，因为字符串就是字符按一定顺序构成的序列，在这一点上三者并没有什么区别。
# 我们推荐大家使用列表的生成式语法来创建列表