## day_19
## 函数的高级应用（装饰器、函数的递归）

## 装饰器
# 装饰器是Python中用一个函数装饰另外一个函数或类并为其提供额外功能的语法现象。
# 装饰器本身是一个函数，它的参数是被装饰的函数或类，它的返回值是一个带有装饰功能的函数。很显然，装饰器是一个高阶函数，它的参数和返回值都是函数。
# eg：(下面这两个不是真的下载和上传函数)

import random
import time
def download(filename):
    print(f"开始下载{filename}")
    time.sleep(random.randint(2,6))
    print(f"{filename}下载完成")

def upload(filename):
    print(f'开始上传{filename}.')
    time.sleep(random.randint(4, 8))
    print(f'{filename}上传完成.')

download('MySQL从删库到跑路.avi')
upload('Python从入门到住院.pdf')

### 如果想知道中间调用函数用了多长时间，只需要用time模块中的time()函数记录一下开始之前和之后的两个时间，相减即可
start=time.time()
download('MySQL从删库到跑路.avi')
end=time.time()
print(f"下载时间：{end-start:.3f}") ## {变量:.3f}用来控制三位小数的输出

start = time.time()
upload('Python从入门到住院.pdf')
end = time.time()
print(f'花费时间: {end - start:.3f}秒')

### 我们发现上面的start=…… end=…… 实际上都是重复的代码，避免这些重复，我们就可以用装饰器
# 如何不写重复代码的前提下，用一种简单优雅的方式记录下函数的执行时间呢？在Python中，装饰器就是解决这类问题的最佳选择。
# 我们可以把记录函数执行时间的功能封装到一个装饰器中，在有需要的地方直接使用这个装饰器就可以了，代码如下所示：
import time
## 定义装饰器函数，它的参数是被装饰的函数或类
def record_time(func): ## 这里的func是传入我们本身的函数，这里是download和upload，对这两个函数记录时间
    # 定义一个带装饰功能（记录被装饰函数的执行时间）的函数
    # 因为不知道被装饰的函数有怎样的参数所以使用*args和**kwargs接收所有参数
    # 在Python中函数可以嵌套的定义（函数中可以再定义函数）
    def wrapper(*args, **kwargs):
        # 在执行被装饰的函数之前记录开始时间
        start = time.time()
        # 执行被装饰的函数并获取返回值
        result = func(*args, **kwargs)
        # 在执行被装饰的函数之后记录结束时间
        end = time.time()
        # 计算和显示被装饰函数的执行时间
        print(f'{func.__name__}执行时间: {end - start:.3f}秒')
        # 返回被装饰函数的返回值（装饰器通常不会改变被装饰函数的执行结果）
        return result
    return wrapper ## 返回wrapper，原因是我们后序在主程序中通过调用record_time就能覆盖原函数来使得原函数具有装饰器的功能

## 使用上面的装饰器函数有两种方式：
# 第一种方式就是直接调用装饰器函数，传入被装饰的函数并获得返回值，我们可以用这个返回值直接覆盖原来的函数，
# 那么在调用时就已经获得了装饰器提供的额外的功能（记录执行时间）
download = record_time(download) ## 调用装饰器的函数覆盖掉本身这个函数，这样函数就获得了装饰器定义的功能
upload = record_time(upload)
download('MySQL从删库到跑路.avi')
upload('Python从入门到住院.pdf')

## 语法糖
# 在Python中，使用装饰器很有更为便捷的**语法糖**（编程语言中添加的某种语法，这种语法对语言的功能没有影响，但是使用更加方法，代码的可读性也更强）
# 可以用`@装饰器函数`将装饰器函数直接放在被装饰的函数上，效果跟上面的代码相同
import random
import time
## 定义装饰器函数和上面一模一样，就定义一个装饰器函数（以func作为一个参数），在装饰器函数里面再定义一个带有其他功能的函数
def record_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f'{func.__name__}执行时间: {end - start:.3f}秒')
        return result
    return wrapper

## 调用装饰器函数，在定义一个新函数的前面加上 @装饰器函数名称，这样使得我们新定义的函数除了有自己定义的功能之外，还有装饰器函数的功能
@record_time
def download(filename):
    print(f'开始下载{filename}.')
    time.sleep(random.randint(2, 6))
    print(f'{filename}下载完成.')

@record_time
def upload(filename):
    print(f'开始上传{filename}.')
    time.sleep(random.randint(4, 8))
    print(f'{filename}上传完成.')

download('MySQL从删库到跑路.avi')
upload('Python从入门到住院.pdf')

# note：我们通过装饰器语法糖为`download`和`upload`函数添加了装饰器，这样调用`download`和`upload`函数时，会记录下函数的执行时间。
# 事实上，被装饰后的`download`和`upload`函数是我们在装饰器`record_time`中返回的`wrapper`函数，调用它们其实就是在调用`wrapper`函数，所以拥有了记录函数执行时间的功能。

## 如果希望取消装饰器的作用，那么在定义装饰器函数的时候，需要做一些额外的工作。
# Python标准库`functools`模块的`wraps`函数也是一个装饰器，我们将它放在`wrapper`函数上，这个装饰器可以帮我们保留被装饰之前的函数，
# 这样在需要取消装饰器时，可以通过被装饰函数的`__wrapped__`属性获得被装饰之前的函数。

## 在装饰器函数里面定义新函数的时候加上 @wraps 装饰器，这样就会为我们调用装饰器函数后的函数增加一个__wrapped__属性，就是保存我们的原函数
import random
import time
from functools import wraps
def record_time(func):
    ## 语法糖调用warps装饰器函数
    @wraps(func) ## 这里要声名wrap的是哪个函数，这是@wrap需要的，否则会有：AttributeError: 'str' object has no attribute '__module__'
    def wrapper(*args,**kwargs): ## 这些参数是给原函数用的
        start=time.time()
        result=func(*args,**kwargs) ## 这里其实是因为装饰器一般不改变原来函数的输出，只是改变它的一些功能，所以最后要return原函数的结果
        end=time.time()
        print(f"{func.__name__}的运行时间为{end-start:.3f}")
        return result ## 装饰器函数不改变原函数的输出
    return wrapper ## 返回新定义的函数，将来可以覆盖掉原函数使得原函数获得装饰器的功能

@record_time
def download(filename):
    print(f"{filename}开始下载")
    time.sleep(random.randint(2, 6))
    print(f"{filename}下载完成")

@record_time
def upload(filename):
    print(f"{filename}开始上传")
    time.sleep(random.randint(2, 6))
    print(f"{filename}上传完成")

## 调用装饰器
download('MySQL从删库到跑路.avi')
upload('Python从入门到住院.pdf')

## 取消装饰器
download.__wrapped__('MySQL必知必会.pdf')
upload = upload.__wrapped__
upload('Python从新手到大师.pdf')

## 装饰器函数本身也可以参数化:
# 简单的说就是通过我们的装饰器也是可以通过调用者传入的参数来定制的,(后面会再提到)。
# 除了可以用**函数**来定义装饰器之外，通过定义**类**的方式也可以定义装饰器。
# 如果一个类中有名为`__call__`的魔术方法，那么这个类的对象就可以像函数一样调用（即这个类所创建出来的对象实际上就是一个函数）
# 这就意味着这个对象可以像装饰器一样工作，代码如下所示。
class Recordtime:
    def __call__(self,func): ## 这样Recordtime这一类的对象就可以像函数一样被调用——装饰器
        @wraps(func)
        def wrapper(*args,**kwargs):
            start=time.time()
            result=func(*args,**kwargs)
            end=time.time()
            print(f"{func.__name__}的运行时间为{end-start:.3f}")
            return result
        return wrapper

## 用装饰器语法糖来构建函数
@Recordtime() ## 这里要加上()，如果用类的方式来构建装饰器
def download(filename):
    print(f'开始下载{filename}.')
    time.sleep(random.randint(2, 6))
    print(f'{filename}下载完成.')

def upload(filename):
    print(f'开始上传{filename}.')
    time.sleep(random.randint(4, 8))
    print(f'{filename}上传完成.')

# 直接创建对象并调用对象传入被装饰的函数
upload = Recordtime()(upload)
download('MySQL从删库到跑路.avi')
upload('Python从入门到住院.pdf')

# note：以上两种添加装饰器的方式：一是通过定义为函数再用语法糖，二是通过定义为类，再调用这个类创建的对象
# 由于`RecordTime`是一个类，所以需要先创建对象，才能把对象当成装饰器来使用，所以提醒大家注意`RecordTime`后面的圆括号，那是调用构造器创建对象的语法。（如list,tuple,dict等类）
# 如果为`RecordTime`类添加一个`__init__`方法，就可以实现对装饰器的参数化，刚才我们说过了，这个知识点等用上的时候再为大家讲解。
# 使用装饰器还可以装饰一个类，为其提供额外的功能，这个知识点也等我们用到的时候再做讲解。

## 递归调用
# Python中允许函数嵌套定义，也允许函数之间相互调用，而且一个函数还可以直接或间接的调用自身，称为递归调用。
# 现实中，有很多问题的定义本身就是一个递归定义，例如我们之前讲到的阶乘，非负整数`N`的阶乘是`N`乘以`N-1`的阶乘，即`N! = N * (N-1)!`，
# 定义的左边和右边都出现了阶乘的概念，所以这是一个递归定义。既然如此，我们可以使用递归调用的方式来写一个求阶乘的函数，代码如下所示：
def fac(num):
    if num in (0,1):
        return 1
    else:
        return num*fac(num-1)
# 上面的代码中，`fac`函数中又调用了`fac`函数，这就是所谓的递归调用。
# 代码第182行的`if`条件叫做递归的收敛条件，简单的说就是什么时候要结束函数的递归调用，在计算阶乘时，如果计算到`0`或`1`的阶乘，就停止递归调用，直接返回`1`；
# 代码第185行的`num * fac(num - 1)`是递归公式，也就是阶乘的递归定义。
#
# 下面，我们简单的分析下，如果用`fac(5)`计算`5`的阶乘，整个过程会是怎样的:
# 递归调用函数入栈
# 5 * fac(4)
# 5 * (4 * fac(3))
# 5 * (4 * (3 * fac(2)))
# 5 * (4 * (3 * (2 * fac(1))))
# 停止递归函数出栈，收敛
# 5 * (4 * (3 * (2 * 1)))
# 5 * (4 * (3 * 2))
# 5 * (4 * 6)
# 5 * 24
# 120
print(fac(5))    # 120

# note：函数调用会通过内存中称为“栈”（stack）的数据结构来保存当前代码的执行现场，函数调用结束后会通过栈恢复之前的执行现场。
# 每进入一个函数调用，栈就会增加一层栈帧（stack frame），栈帧就是我们刚才提到的保存当前代码执行现场的结构；每当函数调用结束后，栈就会减少一层栈帧。
# 通常，内存中的栈空间很小，因此递归调用的次数如果太多，会导致栈溢出（stack overflow），所以**递归调用一定要确保能够快速收敛**。
# 我们可以尝试执行`fac(5000)`，看看是不是会提示`RecursionError`错误，
# 错误消息为：`maximum recursion depth exceeded in comparison`（超出最大递归深度），其实就是发生了栈溢出。

# 我们使用的Python官方解释器，默认将函数调用的栈结构最大深度设置为`1000`层。如果超出这个深度，就会发生上面说的`RecursionError`。
# 我们可以使用`sys`模块的`setrecursionlimit`函数来改变递归调用的最大深度，例如：`sys.setrecursionlimit(10000)`
# 这样就可以让上面的`fac(5000)`顺利执行出结果，但是我们不建议这样做，因为让递归快速收敛才是我们应该做的事情，否则就应该考虑使用循环递推而不是递归。

# 生成斐波那契数列的例子，因为斐波那契数列前两个数都是`1`，从第3个数开始，每个数是前两个数相加的和,记为`f(n) = f(n - 1) + f(n - 2)`
def fib(n):
    if n==1 or n==2:
        return 1
    else:
        return fib(n-1)+fib(n-2)

for i in range(1,20):
    print(fib(i),end='\t')

## 上面的递归调用看起来很酷，但是在实际的使用中，尽量减少使用，因为会大量的占用内存，因此如果是多层的递归，最好是改成循环递推
## 我们比较一下执行时间

## 递归
def fib(n):
    if n==1 or n==2:
        return 1
    else:
        return fib(n-1)+fib(n-2)

start=time.time()
print(fib(99)) ## 输出第99个斐波那契数
end=time.time()
print(f"{end-start:.3f}")

## 循环递推
def fib_2(n):
    result=[1,1]
    if n==1 and n==2:
        return result[0]
    else:
        for i in range(3,n+1):
            result.append(result[i-2]+result[i-3])
        return result[n-1]

start=time.time()
print(fib_2(99)) ## 输出第30个斐波那契数
end=time.time()
print(f"{end-start:.3f}")

## 斐波那契的优雅写法，利用Python的数据交换
def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

# 总结：
# 装饰器是Python中的特色语法，可以通过装饰器来增强现有的类或函数，这是一种非常有用的编程技巧。
#
# 一些复杂的问题用函数递归调用的方式写起来真的很简单，但是函数的递归调用一定要注意收敛条件和递归公式：
# 找到递归公式才有机会使用递归调用，而收敛条件确定了递归什么时候停下来。
# 函数调用通过内存中的栈空间来保存现场和恢复现场，栈空间通常都很小，所以递归如果不能迅速收敛，很可能会引发栈溢出错误，从而导致程序的崩溃。