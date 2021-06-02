## 分支和循环的训练，都是些老程序了

## eg1：寻找水仙花数
# 水仙花数也被称为超完全数字不变数、自恋数、自幂数、阿姆斯特朗数，它是一个3位数，
# 该数字每个位上数字的立方之和正好等于它本身，例如：1^3+5^3+3^3 =153
'''
for i in range(100,1000):
    bai=int(i/100)%10 ## 这里其实写复杂了，可以通过//（整除）来实现
    shi=int(i/10)%10
    ge=int(i)%10

    lifanghe=bai**3+shi*shi*shi+ge*ge*ge
    if(lifanghe == i):
        print(i)
'''

## eg2：正整数翻转（主要还是训练分解数位的能力）
'''
a=int(input("输入正整数："))
reverse_a=0
while a>0:
    reverse_a=reverse_a*10+a%10
    a=a//10
print(reverse_a)
## 这里的思路还挺有趣的，之前我的思路都得先统计数位，要多一遍循环，这里是直接通过移动来完成了
'''

## eg3：百钱百鸡问题。
# 公鸡5元一只，母鸡3元一只，小鸡1元三只，用100块钱买一百只鸡，问公鸡、母鸡、小鸡各有多少只？
'''
for i in range(1,21):
    for j in range(1,34):
        z=100-i-j
        if(5*i+3*j+z//3== and z%3==0): ## 这需要一个边界条件，即要符合小鸡数量是钱的3倍
             print(f"公鸡：{i}只，母鸡：{j}只，小鸡：{z}只")
'''

## eg4：CRAPS赌博游戏
'''
CRAPS又称花旗骰，是美国拉斯维加斯非常受欢迎的一种的桌上赌博游戏。
该游戏使用两粒骰子，玩家通过摇两粒骰子获得点数进行游戏。
简化后的规则是：玩家第一次摇骰子如果摇出了7点或11点，玩家胜；
玩家第一次如果摇出2点、3点或12点，庄家胜；玩家如果摇出其他点数则玩家继续摇骰子，如果玩家摇出了7点，庄家胜；
如果玩家摇出了第一次摇的点数，玩家胜；其他点数玩家继续摇骰子，直到分出胜负。
'''
'''
import random
## 我们初始化玩家有1000块钱的money
money=1000
while money>0:
    debt=int(input("请输入你的赌注："))
    shake_1=random.randint(1,6) ## 在1-6之间随机产生一个
    shake_2=random.randint(1,6)
    sum=shake_1+shake_2
    i=1
    ## 第一次摇色子
    if sum==7 or sum==11:
        print(f"你第{i}次摇出了{sum}点")
        print("Your win")
        money=money+debt
        continue

    if sum==2 or sum==3 or sum==12:
        print(f"你第{i}次摇出了{sum}点")
        print("Your fail")
        money=money-debt
        continue
    
    else:
        print(f"你第{i}次摇出了{sum}点")
        while 1: ## 第2-n次摇色子
            shake_3=random.randint(1,6) ## 在1-6之间随机产生一个
            shake_4=random.randint(1,6)
            i=i+1
            sum_2 = shake_3+shake_4
            if(sum_2==sum):
                print(f"你第{i}次摇出了{sum_2}点")
                print("Your win")
                money=money+debt
                break
            if(sum_2==7):
                print(f"你第{i}次摇出了{sum_2}点")
                print("Your fail")
                money=money-debt
                break
            else:
                print(f"你第{i}次摇出了{sum_2}点")
                continue
print("game over")
'''

## eg5：斐波那契数列
# 斐波那契数列的特点是数列的前两个数都是1，从第三个数开始，每个数都是它前面两个数的和
# 按照这个规律，斐波那契数列的前10个数是：`1, 1, 2, 3, 5, 8, 13, 21, 34, 55`。
# 输出从1到20的斐波那契数列
# 前两个数都是1
from typing import Counter


a, b = 1, 1  ## 这里是一种比较有趣的赋值方式，变量1，变量2= 值1，值2
print(a, b, end=' ')
# 通过递推公式算出后面的18个数
for _ in range(18):
    a, b = b, a + b ## 对应上面所说，a=b,b=a+b
    print(b, end=' ')

## 改进：输出偶数个斐波那契数
a=int(input("输入偶数："))
num_1=1
num_2=1
count=2
print(f"{num_1} {num_2}",end=' ')
while count<a:
    num_1=num_1+num_2
    num_2=num_2+num_1
    print(f"{num_1} {num_2}",end=' ')
    count=count+2
## 个人还是喜欢用数列
