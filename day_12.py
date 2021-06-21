## day_12 
## list和tuple的应用
'''
## eg1：成绩表和平均分统计
# 说明：录入5个学生3门课程的考试成绩，计算每个学生的平均分和每门课的平均分。
## 这在之前嵌套list中有提到，本质上是构建一个嵌套列表（对应C语言二维数组）来保存一个矩阵
scores=[[0]*3 for _ in range(5)] ## [0]*3，构成[0,0,0]，重复五次，生成嵌套列表

## 定义人名和科目
names = ['关羽', '张飞', '赵云', '马超', '黄忠']
courses = ['语文', '数学', '英语']
## 用生成式来生成嵌套列表
scores = [[0]*len(courses) for _ in range(len(names))]
# 录入数据
for i, name in enumerate(names):
    print(f'请输入{name}的成绩 ===>')
    for j, course in enumerate(courses):
        scores[i][j] = float(input(f'{course}: '))
print()
print('-' * 5, '学生平均成绩', '-' * 5)
# 计算每个人的平均成绩
for index, name in enumerate(names):
    avg_score = sum(scores[index]) / len(courses)
    print(f'{name}的平均成绩为: {avg_score:.1f}分')
print()
print('-' * 5, '课程平均成绩', '-' * 5)
# 计算每门课的平均成绩
for index, course in enumerate(courses):
    # 用生成式从scores中取出指定的列创建新列表
    curr_course_scores = [score[index] for score in scores]
    avg_score = sum(curr_course_scores) / len(names)
    print(f'{course}的平均成绩为：{avg_score:.1f}分')

## 这边有个有意思的函数注意一下
# 循环遍历列表的两种方法，一种是通过索引循环遍历，一种是直接遍历列表元素。
# 通过`enumerate`处理后的列表在循环遍历时会取到一个二元组，解包之后第一个值是索引，第二个值是元素
# eg:
list_1=['Python', 'Java', 'Go', 'Swift']

for index in range(len(list_1)):
    print(f"{index}:{list_1[index]}")

for index, element in enumerate(list_1):
    print(f"{index}:{element}")

## 简单来说，就是可以通过enumerate()函数，把list转化成一个嵌套list，第一个元素是下标，第二个元素就是下标对应元素的值

## eg2：设计一个函数返回指定日期是这一年的第几天。

date=str(input("请输入日期(以年-月-日格式)："))

point=[date.find('-'),date.rfind('-')]

year=int(date[:point[0]:])
month=int(date[point[0]+1:point[1]:])
day=int(date[point[1]+1:len(date):])

def which_day(year,month,day):
    ## 求该年是平年还是闰年
    if(year%100==0):
        if(year%400==0):
            year_flag=1
        else:
            year_flag=0
    else:
        if(year%4==0):
            year_flag=1
        else:
            year_flag=0
    
    list_0=(0,31,28,31,30,31,30,31,31,30,31,30,31)
    list_1=(0,31,29,31,30,31,30,31,31,30,31,30,31)
    day_num=0

    if(month<=2):
        for i in range(month):
            day_num=day_num+list_1[i]
        day_num=day_num+day
        return day_num
    
    else:
        if(year_flag==1):
            for i in range(month):
                day_num=day_num+list_1[i]
            day_num=day_num+day
            return day_num
        else:
            for i in range(month):
                day_num=day_num+list_0[i]
            day_num=day_num+day
            return day_num

print(which_day(year,month,day))

## eg3：双色球随机选号
# 说明：双色球属乐透型彩票范畴，由中国福利彩票发行管理中心统一组织发行，在全国范围内销售。
# 红球号码范围为01～33，蓝球号码范围为01～16。双色球每期从33个红球中开出6个号码，从16个蓝球中开出1个号码作为中奖号码，
# 双色球玩法即是竞猜开奖号码的6个红球号码和1个蓝球号码。
import random

red_ball_list=[random.randint(1,33) for _ in range(6)]
blue_ball_list=[random.randint(1,16) for _ in range(1)]

print(f"红球为：{sorted(red_ball_list)}，篮球为：{blue_ball_list}")
'''
## eg4：幸运的女人
# 有15个男人和15个女人乘船在海上遇险，为了让一部分人活下来，不得不将其中15个人扔到海里，有个人想了个办法让大家围成一个圈，
# 由某个人开始从1报数，报到9的人就扔到海里面，他后面的人接着从1开始报数，报到9的人继续扔到海里面，直到将15个人扔到海里。
# 最后15个女人都幸免于难，15个男人都被扔到了海里。
# 问这些人最开始是怎么站的，哪些位置是男人，哪些位置是女人。

die_index=[]
conditions=[True]*30

die_num=0
index=0
number=0

while die_num<15:
    if(conditions[index]):
        number+=1
        if(number==9):
            number=0
            conditions[index]=False
            die_num=die_num+1
            die_index.append(index)
        index+=1
        index=index%30
print(die_index)




