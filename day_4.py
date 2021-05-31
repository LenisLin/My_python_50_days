## 分支结构
## if/else/elif
'''
不同于C++、Java等编程语言，Python中没有用花括号来构造代码块,而是使用了缩进的方式来表示代码的层次结构。
如果`if`条件成立的情况下需要执行多条语句，只要保持多条语句具有相同的缩进就可以了。
换句话说连续的代码如果又保持了相同的缩进那么它们属于同一个代码块，相当于是一个执行的整体。
'''
## if/else后面都有一个:

## eg1：求分段函数值
x=int(input("输入自变量：")) ## python没有double类型的变量
if(x>1):
    y=3*x-5
elif(x>=-1 & x<=1):
    y=x+2
else:
    y=5*x+3
print("因变量y=%d"%y)

## 分支可以嵌套，《python之禅》：“Flat is better than nested”。扁平化最好，少点嵌套。

## note:python中与的表示是用 or 不是用C的&&或者是R的&

##eg2：百分制分数转化为等级分数
score=float(input("请输入百分制成绩："))
if(score>=90):
    print("A")
elif(score>=80.0): ## elif是if else的缩写，自动排除了不满足if的情况
    print("B")
elif(score>=70.0):
    print("C")
elif(score>=60.0):
    print("D")
else:
    print("E")

## eg3：输入三角形三边长，计算三角形的周长和面积
a=float(input("a="))
b=float(input("b="))
c=float(input("c="))

if(a+b>c and b+c>a and a+c>b):
    print("周长：%.2f"%(a+b+c))
    half=(a+b+c)/2
    print("面积：%.2f"%(half*(half-a)*(half-b)*(half-c)**0.5))
else:
    print("ERROR")

## 反正分支就是if/else/elif，然后用冒号和缩进来表示模块