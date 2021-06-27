## day_13
## 集合
## 集合的数学特性：确定性（可以用in/not in来判断是否有这个元素），无序性（不支持索引运算），互异性（不能有重复元素）
## 集合的成员运算性能要比列表好（底层存储决定，具体后面会再提到）

## 创建集合
set_1 = {0} ## 里面至少要有一个元素，如果是{}不是空集合是**空字典**

set_2 = set() ## 用set()构造器构造一个空集合

set_3 = set("hello") ## 将字符串转化成集合
print(set_3)

set_4 = set([1,2,3,4,4,3,2]) ## 将list转化为set，可以用来去重复

set_5 = {x for x in range(1,50) if x%5==0 } ## 利用生成式来创建set
print(set_5)

# note：集合中的元素必须是`hashable`类型。所谓`hashable`类型指的是能够计算出哈希码的数据类型。
# 通常不可变类型都是`hashable`类型，如整数、浮点、字符串、元组等，而可变类型都不是`hashable`类型，如：集合，列表
# 集合本身是可变类型（不是hashable类型），所以集合不能够作为集合中的元素

## 集合的运算
# 检查成员是否属于集合
set1 = {11, 12, 13, 14, 15}
set2 = {'Python', 'Java', 'Go', 'Swift'}
print(1 in set1)
print('Swift' in set2)

# 交并差运算
set1 = {1, 2, 3, 4, 5, 6, 7}
set2 = {2, 4, 6, 8, 10}

# 交集
# 方法一: 使用 & 运算符
print(set1&set2) ## {2, 4, 6}
# 方法二：使用.intersection()方法（注意是方法，不是函数，是set这个类自定义的方法）
print(set1.intersection(set2)) ## {2, 4, 6}

# 并集
# 方法一: 使用 | 运算符
print(set1|set2)
# 方法二: 使用union方法
print(set1.union(set2))

# 差集（a有b没有的叫差集，等于a去掉a&b）
# 方法一: 使用 - 运算符
print(set1 - set2) ## {1, 3, 5, 7}
# 方法二: 使用difference方法
print(set1.difference(set2)) ## {1, 3, 5, 7}

# 对称差(a-b|b-a，a和b的差集的并集，也等价于(a|b)-(a&b))
# 方法一: 使用 ^ 运算符
print(set1^set2) ## {1, 3, 5, 7, 8, 10}
# 方法二: 使用symmetric_difference方法
print(set1.symmetric_difference(set2)) ## {1, 3, 5, 7, 8, 10}
# 方法三: 对称差相当于两个集合的并集减去交集
print((set1|set2)-(set1&set2)) ## {1, 3, 5, 7, 8, 10}
# 方法四: 对称差相当于两个集合差集的并集
print((set1-set2)|(set2-set1)) ## {1, 3, 5, 7, 8, 10}

# 交并差和赋值的联合运算
print(set1,set2) ## {1, 2, 3, 4, 5, 6, 7} {2, 4, 6, 8, 10}
set1 |= set2 ## 先并再赋值，等价于set1=set1 | set2
print(set1) ## {1, 2, 3, 4, 5, 6, 7, 8, 10}

## 比较运算
# == 和 != 判断两个集合的元素是否相同，返回bool值
set1 = {1, 3, 5}
set2 = {1, 2, 3, 4, 5}
set3 = set2
print(set1==set3)
print(set2==set3)

# < 判断是否为子集，<=判断是否为真子集，返回Bool值
print(set1<set2)
print(set1 <= set2)
print(set1.issubset(set2)) ## .issubset()方法也可以判断子集

# > 判断是否为超集（a如果是b子集，b就是a的超集）
print(set2 > set1)
print(set2.issuperset(set1)) ## .issuperset()方法也可以判断超集

## 集合的其他方法
# .add() 增加集合中的元素
set1=set()
set1.add(33)
set1.add(55)
print(set1) ## {33, 55}
set1.add(100,10,1) ## 这样是不行的 .add()方法只能增加一个元素
## 如果要一次性增加多个元素，就要用.update({e1,e2……})的方法
set1.update({100,10,1})
print(set1) ## {33, 1, 100, 55, 10}

# .discard() 删除集合中的指定元素
print(set1) ## {33, 1, 100, 55, 10}
set1.discard(10)
print(set1) ## {33, 1, 100, 55}
set1.discard(2) ## 虽然集合里没有2这个元素，但是.discard()方法依旧不会报错

# .remove()也可以删除元素，但是如果没有这个元素就会报key error，因此如果要用remove最好先判断这个元素是否存在
set1.remove(2)

if 2 in set1:
    set1.remove(2)

# .pop()方法，随机从集合里面删除并返回一个元素
print(set1) ## {1, 100, 55, 33}
set1.pop()
print(set1) ## {1, 100, 55}

# .clear()，清空集合
print(set1) ## {1, 100, 55}
set1.clear()
print(set1) ## set()

# .isdisjoint()，判断两个集合有没有共同元素，没有共同元素返回True，有就返回False
# disjoint sets：不相交的集合，joint：关节，相同的
set1 = {'Java', 'Python', 'Go', 'Kotlin'}
set2 = {'Kotlin', 'Swift', 'Java', 'Objective-C', 'Dart'}
set3 = {'HTML', 'CSS', 'JavaScript'}
print(set1.isdisjoint(set2)) ## False
print(set1.isdisjoint(set3)) ## True

## 不可变集合（frozenset）
# 不可变类型的集合，名字叫`frozenset`。`set`跟`frozenset`的区别就如同`list`跟`tuple`的区别。
# `frozenset`由于是不可变类型，能够计算出哈希码，因此它可以作为`set`中的元素。
# 除了不能添加和删除元素，`frozenset`在其他方面跟`set`基本是一样的。

set1 = frozenset({1, 3, 5, 7})
set2 = frozenset(range(1, 6))
print(set1 & set2)    # frozenset({1, 3, 5})
print(set1 | set2)    # frozenset({1, 2, 3, 4, 5, 7})
print(set1 - set2)    # frozenset({7})
print(set1 < set2)    # False

### 简单的总结
## Python中的集合底层使用了**哈希存储**的方式。
## **集合是一种容器**，元素必须是`hashable`类型，与列表不同的地方在于集合中的元素**没有序**、**不能用索引运算**、**不能重复**。

