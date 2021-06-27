## day_14
## 字典
## 目前已有的容器数据类型：list（列表）、tuple（元组）、set（集合）

# Python程序中的字典跟现实生活中的字典很像，它以键值对（键和值的组合）的方式把数据组织到一起，我们可以通过键找到与之对应的值并进行操作。
# 就像《新华字典》中，每个字（键）都有与它对应的解释（值）一样，每个字和它的解释合在一起就是字典中的一个条目，而字典中通常包含了很多个这样的条目。
# 简单来说，dict（字典），通过key:value的方式来保存一个元素，不同元素之间用逗号隔开，最外面加上一个{}

## 创建字典
## 方法一：{key:value}
from os import name
from typing import Counter


person = {
    'name': '王大锤', 'age': 55, 'weight': 60, 'office': '科华北路62号', 
    'home': '中同仁路8号', 'tel': '13122334455', 'econtact': '13800998877'
}
print(person)

## 方法二：dict()，构造器创建字典
person = dict(name='王大锤', age=55, weight=60, home='中同仁路8号') ## 注意用dict()生成的字典，()里面的key-value对用"="连接
print(person)

## 方法三：字典生成式
item={x:x*3 for x in range(1,10)}
print(item)

## 方法四：python内置函数,zip(),    dict(zip()),生成两个序列的对应位置的字典成员
a="12345"
b="abcde"
c=dict(zip(a,b)) ## zip()只是压缩两个对象，只有转化成dict才会是字典
print(c)
# 总结：字典来保存一个人的信息远远优于使用列表或元组，因为我们可以用`:`前面的键来表示条目的含义，而`:`后面就是这个条目所对应的值。

## 字典的遍历
person = {'name': '王大锤', 'age': 55, 'weight': 60, 'office': '科华北路62号'}
print(len(person)) ## len(dict())返回的就是字典Key的个数

for i in person:
    print(i) ## 如果对于字典元素进行遍历，遍历的是key值

## 字典的运算
# note：对于字典类型来说，成员运算可以判定指定的键在不在字典中，索引运算可以通过键获取对应的值或者向字典中加入新的键值对。
# 值得注意的是，字典的索引不同于列表的索引，列表中的元素因为有属于自己有序号，所以列表的索引是一个整数；
# 字典中因为保存的是键值对，所以字典的索引是键值对中的键，通过索引操作可以修改原来的值或者向字典中存入新的键值对。
# 特别提醒，**字典中的键必须是不可变类型**，例如整数（int）、浮点数（float）、字符串（str）、元组（tuple）等类型的值；
# 显然，列表（list）和集合（set）是不能作为字典中的键的，字典类型本身也不能再作为字典中的键，因为字典也是可变类型，但字典可以作为字典中的值。

## 成员运算
person = {'name': '王大锤', 'age': 55, 'weight': 60, 'office': '科华北路62号'}
print("name" in person, "tel" in person) ## 返回一个bool值，判断keys是否存在

## 索引运算
# [key]索引key对应的value，这里注意,这个key必须是跟定义的类型是一样的，这里age是str类型的，因此就得用""来索引
print(person['age']) ## 如果索引的key不在dict中，就会有key error

# 修改某个key对应的value
if 'age' in person:
    person['age'] = 25
print(person)

# 增减新的key:value
if("tel" not in person):
    person["tel"]='123456'
print(person)

# dict中的key数量
print(len(person))

# 遍历dict中的key:value对
for i in person: ## for遍历一个字典，就直接遍历了key值，因此不需要像也不合适用range(1,len())来生成序号了，毕竟不是List
    print(f"k{i}:{person[i]}") 

## 字典的方法
# 嵌套字典，字典中的值又是一个字典(嵌套的字典)
## eg：用号码来作为students的key，value用另一个字典来呈现
students = {
    1001: {'name': '狄仁杰', 'sex': True, 'age': 22, 'place': '山西大同'},
    1002: {'name': '白元芳', 'sex': True, 'age': 23, 'place': '河北保定'},
    1003: {'name': '武则天', 'sex': False, 'age': 20, 'place': '四川广元'}
} 

## 用.get(key)来索引value值，如果key不存在不会报错，只会返回none或者默认值
print(students.get(1001)) ## {'name': '狄仁杰', 'sex': True, 'age': 22, 'place': '山西大同'}
print(students.get(1004)) ## None

## 获取字典中所有的keys
print(students.keys()) ## dict_keys([1001, 1002, 1003])

## 获取字典中所有的value
print(students.values()) ## dict_values([{'name': '狄仁杰', 'sex': True, 'age': 22, 'place': '山西大同'}, {'name': '白元芳', 'sex': True, 'age': 23, 'place': '河北保定'}, {'name': '武则天', 'sex': False, 'age': 20, 'place': '四川广元'}])

## 获取字典中所有的key:value
print(students.items())

## 利用.items()进行循环遍历
for key,value in students.items():
    print(key,"---",value)

## .pop()，删除某个key-value对，并且返回它们的值
stu_1=students.pop(1001)
print(stu_1)
print(type(stu_1))
print(len(students)) ## 2

stu2 = students.pop(1005, {}) ## 后面这个{}代表默认值，即如果不存在这个key，就返回这个{}
print(stu2)             # {}

## .popitem()方法删除字典中最后一组键值对并返回对应的二元组
stu_3=students.popitem()
print(type(stu_3))
print(stu_3) ## (1003, {'name': '武则天', 'sex': False, 'age': 20, 'place': '四川广元'})
# note：.popitem()和.pop()不同：
# ①前者删除返回最后一个key:value对，后者返回指定key的key:value对
# ②如果没有对应key，前者会报错，后者会输出None或者默认值
# ③前者返回一个key,value的二元组，可以用key,value=dict.popitem()来分别赋值，后者返回一个只有一个元素的字典类型

## .setdefault()更新dict的key-value对或者修改key对应的value值
print(students)
students.setdefault(1005,{'name': '方启鹤', 'sex': True})
print(students)

print(students.setdefault(1005,{'name': '方启鹤', 'sex': True}))
## 这里我们可以直接print()上面那个.setdefault()方法:
# 如果这个键在字典中存在，更新这个键之后会返回原来与这个键对应的值
# 如果这个键在字典中不存在，方法将返回第二个参数的值，默认为None

## .update()，更新字典中的key-value对，这个方法.update()的括号内可以是另一个字典，相当于对于两个字典取并集
## 使用update更新字典元素，相同的键会用新值覆盖掉旧值，不同的键会添加到字典中
print(students)
others = {
    1005: {'name': '乔峰', 'sex': True, 'age': 32, 'place': '北京大兴'},
    1010: {'name': '王语嫣', 'sex': False, 'age': 19},
    1008: {'name': '钟灵', 'sex': False}
}
students.update(others)
print(students)

## del dict[key]，删除dict中的key-value，如果对应的key不存在，会有keyerror错误
print(person)
del person['age']
print(person)
del person["sex"]

## 字典的应用
## 字典其实跟hashmap很像，就是构建了一个映射关系

## eg1:输入一段话，统计每个英文字母出现的次数。
sentence = input("请输入一段话：") ## 不能用str(input())这样输入的就是一个字符串，而不是一个个的字符
Counter={}
for chr in sentence:
    if "A" <= chr <= "Z" or "a" <= chr <= "z": ## python不需要把区间像cpp那样写成一个或
        Counter[chr]=Counter.get(chr,0)+1 ## counter.get(chr,0)就是返回chr对应的value，如果不存在这个key，就输出0，有点妙说实话
for key,value in Counter.items():
    print(f"{key}出现了{value}次")

## eg2：在一个字典中保存了股票的代码和价格，找出股价大于100元的股票并创建一个新的字典。
stocks = {
    'AAPL': 191.88,
    'GOOG': 1186.96,
    'IBM': 149.24,
    'ORCL': 48.44,
    'ACN': 166.89,
    'FB': 208.09,
    'SYMC': 21.29
}
stock={x:y for x,y in stocks.items() if y>100} ## for key,value in dict.items():实现字典所有元素的遍历
print(stock)

## 总结：
# Python程序中的字典跟现实生活中字典非常像，允许我们**以键值对的形式保存数据**，再**通过键索引对应的值**。
# 这是一种非常利于数据检索的数据类型，底层原理我们在后续的课程中再研究。
# 再次提醒大家注意，**字典中的键必须是不可变类型**，字典中的值可以是任意类型。