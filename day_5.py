## 循环
## for-in循环（已知循环次数，常和range搭配）、while循环（不知道循环几次，最后用一个bool值来break）

## eg1：实现常数列0-100求和
'''
sum=0
for i in range(0,101):
    sum=sum+i
print(sum)
'''

## notice：
## range()，可以用来构造一个范围，range(start=a,terminal=b,step=c)，就是从a到b，[a,b)，左闭右开，步长为c。

##eg2：while实现猜数字游戏
'''
import random ## import后面不要加（）
value_random=random.randint(1,100) ## 在1到100之间随机生成一个int数值
counter=0
while 1: ## while 后面要设置条件，一般写while 1或者 while Ture，后面在循环里面再用if来break
    counter +=1
    number=int(input("请输入数字："))
    if(number==value_random): ## if其实不需要（）
        print("Yes")
        break
    else:
        if(number>value_random):
            print("大了")
        else:
            print("小了")
print("你一共猜了%d次"%counter)
'''
'''
notice：
`while True`构造了一个条件恒成立的循环
`break`只能终止它所在的那个循环
`continue`，它可以用来放弃本次循环后续的代码直接让循环进入下一轮。
'''
'''
## eg3：循环嵌套输出九九乘法表
for i in range(1,10):
    for j in range(1,i+1):
        print(f'{i}*{j}={i*j}',end='\t') 
    print()

for i in range(1,10):
    for j in range(1,i+1):
        print('{i}*{j}={i*j}',end='\t') 
    print()
'''
## 这里有些有趣的地方
###### print(f'这里面可以引用变量，用{}括起来即可',end='可以用来控制打印完之后有没有什么结尾')
## print()，可以用来换行

## test1:输入一个数判断是否是素数
"""
num=int(input("请输入一个数："))
flag=0
for i in range(2,int(num/2)):
    if(num%i==0):
        flag=1
        break

if (flag==1):
    print(f"{num}不是素数")
else:
    print(f"{num}是素数")
"""

## test2：输入两个正整数，计算它们的最大公约数和最小公倍数
a=int(input("正整数1="))
b=int(input("正整数2="))

max_1 = max(a,b)
min_1 = min(a,b)

for i in range(min_1,0,-1): ## 判断最大公约数
    if(a%i==0 and b%i==0):
        print(f"最小公约数为{i}")
        break
for j in range(max_1,a*b+1): ## 判断最小公倍数
    if(j%a==0 and j%b==0):
        print(f"最小公倍数为{j}")
        break

'''
总结：
for-in + range(a,b,c):   可以在[a,b)的范围内，步长为c地执行已知次数的循环
while 1/TRUE + break:  可以实现未知次数的循环
'''