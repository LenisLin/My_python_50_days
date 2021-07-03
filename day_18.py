## day_18
## 函数进阶使用

## 关键字参数
def can_form_triangle(a,b,c):
    print(f"a={a},b={b},c={c}")
    return a+b>c and b+c>a and a+c>b

# 调用函数传入参数不指定参数名按位置对号入座
print(can_form_triangle(1, 2, 3))
# 调用函数通过“参数名=参数值”的形式按顺序传入参数
print(can_form_triangle(a=1, b=2, c=3))
# 调用函数通过“参数名=参数值”的形式不按顺序传入参数
print(can_form_triangle(c=3, a=1, b=2))

# 在没有特殊处理的情况下，函数的参数都是**位置参数**，也就意味着传入参数的时候对号入座即可:
# 如上面代码的第11行所示，传入的参数值`1`、`2`、`3`会依次赋值给参数`a`、`b`、`c`。
# 当然，也可以通过`参数名=参数值`的方式传入函数所需的参数，因为指定了参数名，传入参数的顺序可以进行调整，如上面代码的第13行和第15行所示。

# 调用函数时，如果希望函数的调用者必须以`参数名=参数值`的方式传参，可以用命名关键字参数取代位置参数。
# 所谓命名关键字参数，是在函数的参数列表中，写在`*`之后的参数，代码如下所示。

def can_form_triangle(*, a, b, c): ## 参数列表中的`*`是一个分隔符，`*`前面的参数都是位置参数，而`*`后面的参数就是命名关键字参数
    print(f'a = {a}, b = {b}, c = {c}')
    return a + b > c and b + c > a and a + c > b

# TypeError: can_form_triangle() takes 0 positional arguments but 3 were given
# print(is_valid_for_triangle(3, 4, 5))
# 传参时必须使用“参数名=参数值”的方式，位置不重要
print(can_form_triangle(a=3, b=4, c=5))
print(can_form_triangle(c=5, b=4, a=3))

## 可变参数
# 在函数的参数列表中可以使用**可变参数**`*args`来接收任意数量的参数，但是`*args`不能够接收带参数名的参数。
def calc(*args):
    result=0
    for arg in args:
        result+=arg
    return result

print(calc(1,2,3))
print(calc(a=1, b=2, c=3)) ## TypeError: calc() got an unexpected keyword argument 'a'

## 关键字参数
# 在设计函数时，如果既不知道调用者会传入的参数个数，也不知道调用者会不会指定参数名，那么同时使用可变参数和**关键字参数**。
# 关键字参数会将传入的带参数名的参数组装成一个**字典**，**参数名**就是字典中键值对的**键**，而**参数值**就是字典中键值对的**值**。

def calc(*args,**kwargs): ## *args可以用来识别多个位置参数（多个参数形成元组传入），**kwargs可以识别多个关键字参数
    result=0
    for arg in args:
        result+=arg
    for value in kwargs.values(): ## dict.values() 这个方法可以访问dict中的所有value,具体的可以去看day_14复习一下
        result+=value
    return result

print(calc())                  # 0
print(calc(1, 2, 3))           # 6
print(calc(a=1, b=2, c=3))     # 6
print(calc(1, 2, c=3, d=4))    # 10
# print(calc(1,3,a=5,1))         # SyntaxError: positional argument follows keyword argument

# note：**不带参数名的参数（位置参数）必须出现在带参数名的参数（关键字参数）之前**，否则将会引发异常。(我们先定义了*args然后是**kwargs)

# 总结：
# ①函数的参数有位置参数和关键字参数两种
# ②,*,用来分隔有限个位置参数（前）和关键字参数（后）
# ③*args（形成元组），可以用来传入多个位置参数，**kwargs（形成字典），可以用来传入多个关键字参数，位置参数都要在形式参数之前

## 高阶函数用法
# 函数的参数和返回值可以是任意类型的对象，这就意味着**函数本身也可以作为函数的参数或返回值**，这就是所谓的**高阶函数**。

# `calc`函数不仅仅可以做多个参数求和，还可以做多个参数求乘积甚至更多的二元运算，我们就可以使用高阶函数的方式来改写上面的代码，将加法运算从函数中移除掉：
def calc(*args,init_value,op,**kwargs):
    # *args,**kwargs代表位置参数和关键字参数，init_value代表初始值，op是二元运算函数
    # 这里主要是一个op函数，它可以实现对两个元素进行操作，具体什么操作我们还需要再进行另外定义（相当于R里面一个函数的选项）
    result = init_value
    for arg in args:
        result=op(result,arg)
    for value in kwargs.values():
        result=op(result,value)

    return result

# 定义op，相当于给这个函数写选项
def add(x,y):
    return x+y
def mul(x,y):
    return x*y

print(calc(1, 2, 3, init_value=0, op=add, x=4, y=5))      # 15
print(calc(1, 2, x=3, y=4, z=5, init_value=1, op=mul))    # 120

# 通过对高阶函数的运用，`calc`函数不再和加法运算耦合，所以灵活性和通用性会变强，这是编程中一种常用的技巧。
# 需要注意的是，将函数作为参数和调用函数是有显著的区别的，**调用函数需要在函数名后面跟上圆括号，而把函数作为参数时只需要函数名即可**。
# 上面的代码也可以不用定义`add`和`mul`函数，因为Python标准库中的`operator`模块提供了代表加法运算的`add`和代表乘法运算的`mul`函数，我们直接使用即可：
import operator
print(calc(1, 2, 3, init_value=0, op=operator.add, x=4, y=5))      # 15，这里operartor.add作为参数，所以没有()
print(calc(1, 2, x=3, y=4, z=5, init_value=1, op=operator.mul))    # 120

## 其他内置的高阶函数(filter和map)
# filter可以实现对序列中元素的过滤，map可以实现对序列中元素的映射

# eg：去掉一个整数列表中的奇数，并对所有的偶数求平方得到一个新的列表
def is_even(num):
    return num % 2 == 0

def square(num):
    return num ** 2

numbers1 = [35, 12, 8, 99, 60, 52]
numbers2 = list(map(square, filter(is_even, numbers1))) ## map(映射方法，原象) fileter(过滤的方法，过滤的对象)
print(numbers2)    # [144, 64, 3600, 2704]

numbers2=[x**2 for x in numbers1%2==0 ] ## 用列表生成式语法来实现同样的功能
print(numbers2)    # [144, 64, 3600, 2704]

## Lambda函数（匿名函数）
# 使用高阶函数的时候，如果作为参数或者返回值的函数本身非常简单，一行代码就能够完成，那么我们可以使用**Lambda函数**来表示。
# Python中的Lambda函数是没有的名字函数，也叫做**匿名函数**，匿名函数只能有一行代码，代码中的表达式产生的运算结果就是这个匿名函数的返回值。
# 上面代码中的`is_even`和`square`函数都只有一行代码，我们可以用Lambda函数来替换掉它们。

numbers2 = list(map(lambda x:x**2, filter(lambda x:x%2==0, numbers1)))
print(numbers2)    # [144, 64, 3600, 2704]

# 定义Lambda函数的关键字是`lambda`，后面跟函数的参数，如果有多个参数用逗号进行分隔；
# 冒号后面的部分就是函数的执行体，通常是一个表达式（一个函数如果只有一行且只用一次，就可以用lambda），运算结果就是Lambda函数的返回值，不需要return关键字。

# 加减乘除这种简单的二元函数，也可以用Lambda函数来书写，例如调用上面的`calc`函数时，可以通过传入Lambda函数来作为`op`参数的参数值。
# 当然，`op`参数也可以有默认值，例如我们可以用一个代表加法运算的Lambda函数来作为`op`参数的默认值。

def calc(*args, init_value=0, op=lambda x, y: x + y, **kwargs):
    ## op=lambda x,y:x+y，即输入两个参数x和y，lambda的返回值就是x+y，这里定义了op的默认值为加法
    result = init_value
    for arg in args:
        result = op(result, arg)
    for value in kwargs.values():
        result = op(result, value)
    return result

# 调用calc函数，使用init_value和op的默认值（就是上面def里面的那句lambda）
print(calc(1, 2, 3, x=4, y=5))    # 15
# 调用calc函数，通过lambda函数给op参数赋值
print(calc(1, 2, 3, x=4, y=5, init_value=1, op=lambda x, y: x * y))    # 120

# note：上面的代码中的`calc`函数，它同时使用了可变参数、关键字参数、命名关键字参数。
# 其中命名关键字参数要放在可变参数和关键字参数之间，传参时先传入可变参数，关键字参数和命名关键字参数的先后顺序并不重要。

## lambda函数定义一行的函数
# 有很多函数在Python中用一行代码就能实现，我们可以用Lambda函数来定义这些函数，调用Lambda函数就跟调用普通函数一样

## 求阶乘，只要输入一个上界
## `reduce`函数是Python标准库`functools`模块中的函数，它可以实现对数据的归约操作
import operator, functools
fac = lambda num:functools.reduce(operator.mul,range(1,num+1),1)

## 判断是否为素数
# 先用lambda函数构建x，表达式是大于1且满足后面的那个条件
# map(映射方法，原象)，其中映射方法为求余数，原象是从2到根号x所有的数，这样就构建了一个x的从2到根号x的余数的映射
is_prime=lambda x: x>1 and all(map(lambda f:x%f,range(2,int(x**0.5)+1)))

# 调用Lambda函数
print(fac(10))        # 3628800
print(is_prime(9))    # False

# note1:上面使用的`reduce`函数是Python标准库`functools`模块中的函数，它可以实现对数据的归约操作，
# 通常情况下，**过滤**（filter）、**映射**（map）和**归约**（reduce）是处理数据中非常关键的三个步骤，而Python的标准库也提供了对这三个操作的支持。

# note2:上面使用的`all`函数是Python内置函数，如果传入的序列中所有布尔值都是`True`，`all`函数就返回`True`，否则`all`函数就返回`False`。

# 总结
# ①Python中的函数可以使用可变参数`*args`和关键字参数`**kwargs`来接收任意数量的参数，而且传入参数时可以带上参数名也可以没有参数名，
# 可变参数会被处理成一个元组，而关键字参数会被处理成一个字典。
#
# ②Python中的函数也是对象，所以函数可以作为函数的参数和返回值，也就是说，在Python中我们可以使用高阶函数。
# 如果我们要定义的函数非常简单，只有一行代码且不需要名字，可以将函数写成Lambda函数（匿名函数）的形式。