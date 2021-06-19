## day_9 
## 函数和字符串的应用
"""
Q:字符串类型（`str`）可以通过调用方法的方式进行操作，而之前我们用到的数值类型（如`int`、`float`）却没有可以调用的方法。

A:Python中，数值类型是标量类型，也就是说这种类型的变量没有可以访问的内部结构；
而字符串类型是一种结构化的、非标量类型，所以才会有一系列的方法可供调用。
"""

'''
## eg1:设计一个生成指定长度验证码的函数(验证码由数字和英文大小写字母构成。)
import random
all_chars='0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ' ## 可以简化为 ALL_CHARS = string.digits + string.ascii_letters

def key_generate(k_length):
    code = ''
    for i in range(0,k_length): ## 注意，循环注意次数的设置
        index = random.randint(0,len(all_chars)-1)
        code= code+all_chars[index]
    return(code)

## `random`模块的`sample`和`choices`函数都可以实现随机抽样，`sample`实现无放回抽样，这意味着抽样取出的字符是不重复的；
## `choices`实现有放回抽样，这意味着可能会重复选中某些字符。这两个函数的第一个参数代表抽样的总体，而参数`k`代表抽样的数量。

a=int(input("请输入验证码长度："))
b=int(input("请输入验证码的组数"))

## 通过b组来验证函数功能
for i in range(0,b):
    print(f"{key_generate(a)}",end='\t')
'''
'''
## eg2：设计一个函数返回给定文件名的后缀名。
def file_suffix(a):
    index=a.rfind('.')
    if(index<0):
        print("该文件没有后缀")
    elif(index==0):
        print("该文件为隐藏文件") 
    else:
        s=''
        for i in range(index+1,len(a)):
            s=s+a[i]
        print(f"文件的后缀是：{s}")
filename = str(input("请输入文件名："))
file_suffix(filename)

# note:`os.path`模块的`splitext`函数，
# 这个函数会将文件名拆分成带路径的文件名和扩展名两个部分，然后返回一个二元组（下节课会讲到元组），二元组中的第二个元素就是文件的后缀名（包含`.`）
# 类似R里面的strsplit
'''
## eg3:在终端中显示滚动文字。
# 实现跑马灯文字的原理非常简单，把当前字符串的第一个字符放到要输出的内容的最后面，把从第二个字符开始后面的内容放到要输出的内容的最前面，
# 通过循环重复这个操作，就可以看到滚动起来的文字。
# 两次循环之间的间隔可以通过`time`模块的`sleep`函数来实现，而清除屏幕上之前的输出可以使用`os`模块的`system`函数调用系统清屏命令来实现。
import time ## 实现休眠
import os ## 调用操作系统的命令
content = '北 京 欢 迎 你 为 你 开 天 辟 地           '
while True:
    # os.system('cls')  # Windows清除屏幕上的输出
    # os.system('clear') # macOS清除屏幕上的输出
    os.system('cls')
    print(content)
    # 休眠0.2秒（200毫秒）
    time.sleep(0.2)
    content = content[1:] + content[0]
    ## content[1:]，就是从content[1]开始到content[len(content)]

    ## 这个还挺好玩的，不过对我现在帮助不大，所以快速过一下就去学AI了

    ## 总结：一定要有意识的**将相对独立且重复出现的功能封装成函数**
    ## 字符串是非常重要的数据类型，**字符串的常用运算和方法需要掌握**