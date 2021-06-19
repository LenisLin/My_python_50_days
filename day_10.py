## day_10
## 列表list

# Python中我们可以通过容器类型的变量来保存和操作多个数据，数据类型。
# 按照我的理解，数据类型应该有int,float,str，这些可以认为是基本数据类型，而列表，元组，字典这些可以认为是容器数据类型

# **列表是由一系元素按特定顺序构成的数据序列**，这样就意味着定义一个列表类型的变量，**可以保存多个数据**，而且**允许有重复的数据**。
# 跟上一课我们讲到的字符串类型一样，列表也是一种结构化的、非标量类型，操作一个列表类型的变量，除了可以使用运算符还可以使用它的方法。

## 用[]来定义列表
list_1 = [1,2,3,4,5]
list_2 = ["python","cpp","R"]

## 用list()构建列表
# `list`并不是一个函数，而是创建列表对象的构造器。
list_3 =list(range(1,10))

print(list_1,list_2,list_3)

# note:列表是一种可变数据类型，也就是说列表可以添加元素、删除元素、更新元素，这一点跟我们上一课讲到的字符串有着鲜明的差别。
# 字符串是一种不可变数据类型，也就是说对字符串做拼接、重复、转换大小写、修剪空格等操作的时候会产生新的字符串，原来的字符串并没有发生任何改变

## 列表的运算（大部分和字符串很像）
print(list_1+list_2) ## 拼接
print(list_1*3) ## 重复
print("cpp" in list_2) ## 查找成员
print(len(list_2)) ## 判断列表长度（元素个数）
print(list_2[2]) ## 列表索引
print(list_2[0:]) ## 列表切片
print(list_1==list_2) ## 判断元素是否相等
print(list_2 < list_1) ## 判断列表长度，但是前提是这两个list中元素的类型一致，否则有type error

# note：列表是可变类型，所以通过索引操作既可以获取列表中的元素，也可以更新列表中的元素。对列表做索引操作一样要注意索引越界的问题，对于有`N`个元素的列表，
# 正向索引的范围是`0`到`N-1`，负向索引的范围是`-1`到`-N`，如果超出这个范围，将引发`IndexError`异常，错误信息为：`list index out of range`

## 列表的遍历
## 用for遍历
items = ['Python', 'Java', 'Go', 'Kotlin']
for i in range(0,len(items)): ## 通过下标来遍历，注意第一个是从0开始
    print(items[i])
for i in items:
    print(i) ## 利用元素直接遍历

## eg：摇若干次色子，统计每个点数被摇到的次数
import random
a=int(input("输入摇色子的次数："))
b=[0]*6

for i in range(0,a):
    tem=random.randint(1,6)
    b[tem-1]=b[tem-1]+1

for j in range(1,7):
    print(f"摇到{j}点的次数为{b[j-1]}次\n")

## 列表的方法（list_object.function()）
items = ['Python', 'Java', 'Go', 'Kotlin']

## .append()在尾部添加元素
items.append("Rust")
print(items)

## .insert()在指定位置插入元素
print(items)
items.insert(2,"cpp") ## 插入到对应下标的位置，其他的自动后延
print(items)

## 删除指定元素（元素值索引）
items.remove('Rust') ## 如果list中没有这个元素，就会出现value error
print(items)

## 删除对应下标的元素，要保证不越界
print(items)
items.pop(1) ## 只要跟着一个下标即可，类似就是把这个list视作一个堆栈，从中pop出指定位置的元素，同时会输出这个元素，删去list中的这个元素
print(items)
# 也可以用 del item[i] 来删除对应下标的元素，只不过不会返回值

## 清空列表中的元素
print(items)
items.clear()
print(items)

## 元素的位置和次数
items = ['Python', 'Java', 'Java', 'Go', 'Kotlin', 'Python']
# 查找元素位置
print(items.index('Python')) ## 输出第一个'Python'的下标
print(items.index('Python',2)) ## 输出第2个'Python'的下标
# 计算元素出现的次数
print(items.count("Python"))

## 翻转和排序
items = ['Python', 'Java', 'Go', 'Kotlin', 'R']
items.reverse()
print(items) ## note：直接print(item.reverse())是不合法的，原因是因为item.reverse()并不返回一个list，返回一个none

items.sort()
print(items) ## 按照首字母排序

## 创建一个List的方法

## 法一：for + .append()生成新列表（就很像我们C语言创建数组的方法）
## eg1：创建一个0~9的list
list_1 = []
for i in range(0,10):
    list_1.append(i)
print(list_1)

## eg2：创建一个由'hello world'中除空格和元音字母外的字符构成的列表
list_2 = []
for x in "hello world":
    if x not in " aeiou": ## 这个有点秀了，有这种not-in的用法
        list_2.append(x)
print(list_2)

## eg3：创建一个由个两个字符串中字符的笛卡尔积构成的列表
list_3=[]
for i in "ABC":
    for j in "123":
        list_3.append(i+j)
print(list_3)

## 法二：通过生成式来创建list
## eg1：创建一个0~9的list
list_1 = [x for x in range(0,9)] ## 大概的意思
print(list_1)

## eg2：创建一个由'hello world'中除空格和元音字母外的字符构成的列表
list_2 = [x for x in "hello world" if x not in " aeiou"]
print(list_2)

## eg3：创建一个由个两个字符串中字符的笛卡尔积构成的列表
list_3 = [x+y for x in "ABC" for y in "123"]
print(list_3)

## 生成式格式 [生成式的公式 生成条件]

# 生成式性能也优于上面使用`for`循环和`append`方法向空列表中追加元素的方式
# 生成式拥有更好的性能，那是因为Python解释器的字节码指令中有专门针对生成式的指令（`LIST_APPEND`指令）；
# 而`for`循环是通过方法调用（`LOAD_METHOD`和`CALL_METHOD`指令）的方式为列表添加元素，方法调用本身就是一个相对耗时的操作

## 列表的嵌套（双层嵌套就是二维数组）
""" 
Python语言没有限定列表中的元素必须是相同的数据类型，也就是说一个列表中的元素可以任意的数据类型，当然也包括列表。
如果列表中的元素又是列表，那么我们可以称之为嵌套的列表。嵌套的列表可以用来表示表格或数学上的矩阵，
例如：我们想保存5个学生3门课程的成绩，可以定义一个保存5个元素的列表保存5个学生的信息，而每个列表元素又是3个元素构成的列表，分别代表3门课程的成绩。
"""

# note：以下是有问题的创建嵌套列表的方法
scores = [[0] * 3] * 5
print(scores)    # [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]

scores[0][0]=95
print(scores) ## [[95, 0, 0], [95, 0, 0], [95, 0, 0], [95, 0, 0], [95, 0, 0]]
scores[1][1]=100
print(scores) ## [[95, 100, 0], [95, 100, 0], [95, 100, 0], [95, 100, 0], [95, 100, 0]]
## 出现以上这样的原因是因为，list*n，所生成的新list中间的n个元素，其实都是指向了同一个主存单元，因此我们对于其中一个进行修改，就会对所有的进行修改

## 正确的嵌套方法
scores = [[0]*3 for _ in range(0,5)] ## 这里查一下这个下划线的用法
print(scores)
scores[0][0]=100
print(scores)