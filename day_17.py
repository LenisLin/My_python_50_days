## day_17
## 面向对象编程应用

## eg1：扑克游戏
# 使用面向对象编程方法，首先需要从问题的需求中找到对象并抽象出对应的类，此外还要找到对象的属性和行为。
# 我们可以从需求的描述中找出名词和动词，名词通常就是对象或者是对象的属性，而动词通常是对象的行为。
# 扑克游戏中至少应该有三类对象，分别是牌、扑克和玩家，牌、扑克、玩家三个类也并不是孤立的。
# 类和类之间的关系可以粗略的分为**is-a关系（继承）**、**has-a关系（关联）**和**use-a关系（依赖）**。

## 定义花色类型
# 我们可以用0到3的四个数字来代表四种不同的花色，但是这样的代码可读性会非常糟糕，因为我们并不知道黑桃、红心、草花、方块跟0到3的数字的对应关系。
# 如果一个变量的取值只有有限多个选项，我们可以使用枚举。与C、Java等语言不同的是，Python中没有声明枚举类型的关键字，
# 但是可以通过继承`enum`模块的`Enum`类来创建枚举类型。

# C语言的枚举类型，参考资料：https://www.runoob.com/cprogramming/c-enum.html
# C语言中，如果想把一个字符常量定义为一个数字，可以用#define 字符 数字 的方式，如：
# #define MON  1，如果想定义周一~周日，就要有7行define，太麻烦，所以就可以用enum来声明定义一个枚举变量，
# 即7行#define等价于
#enum DAY{
#      MON=1, TUE, WED, THU, FRI, SAT, SUN
#};
# 注意：第一个枚举成员的默认值为整型的 0，后续枚举成员的值在前一个成员上加 1。我们在这个实例中把第一个枚举成员的值定义为 1，第二个就为 2，以此类推。

## 定义花色枚举类型，继承enum中的Enum
from enum import Enum
class Suite(Enum):
    SPADE, HEART, CLUB, DIAMOND=range(4)  ## SPADE, HEART, CLUB, DIAMOND和0-3一一对应，之后访问Suite.suite就会有个数字

## 测试花色枚举类型
if(False):
    for suite in Suite:
        print(f"{suite}:{suite.value}")  ## 对于枚举类型，我们可以理解成是一个字典，字符常量就是Key,对应的int类型就是value
        ## 我们可以用for-in循环遍历枚举类型中的每一个符号常量，通过object.value就可以找到对应的int值

## 定义牌类
# 牌分成两种，一种是手牌，一种是牌堆，都是牌，牌的属性要有花色和点数，并且最好是可以被Print出来面值

## 测试牌对象
if(False):
    card_1=Cards(Suite.SPADE,13)
    print(card_1)

## 定义牌堆类
import random
class Cards:
    def __init__(self,suite,face):
        self.suite=suite
        self.face=face

    def __repr__(self):
        suite_str='♠♥♣♦'
        face_list=['', 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        return (f"{suite_str[self.suite.value]}{face_list[self.face]}")

    def __lt__(self,other): ## 注意“<”需要两个相同type的对象
        if self.suite==other.suite: ## 花色相同比较点数的大小
            return self.face < other.face ## 返回的是一个Ture或者False
        ## 花色不同比较花色对应的值
        return self.suite.value < other.suite.value

class Poker:
    ## 初始化牌堆，有52张牌，每个花色13张牌，作为牌的一个属性
    def __init__(self):
        self.poker_heap=[Cards(suite,face) for suite in Suite for face in range(1,14)]
        ## 当前发牌顺序，从牌堆取牌就可以按照这个来取
        self.current=0
    
    ## 定义洗牌
    def shuffle(self):
        self.current=0
        random.shuffle(self.poker_heap) ## 调用random模块的shuffle函数
    
    ## 定义发牌
    def deal(self):
        if(self.current<52):
            card=self.poker_heap[self.current]
            self.current+=1
            return card

    ## 用于测试，方便阅读
    def __repr__(self):
        return (f"{self.poker_heap}") ## 由于不能直接在__repr__里面返回

## 测试牌堆类
if(False):
    pokers=Poker()
    pokers.shuffle()
    print(pokers)
    a=pokers.deal()
    print(f"{a}")
        

## 定义手牌类，这里我在抽象的时候有点重复定义了，其实这些功能放在player里面就可以了
class hand_card():
    ## 定义手牌属性，现在牌的张数，手牌
    def __init__(self):
        self.hand_card_list=[]
        self.num=0
    
    ## 定义获得牌
    def get_card(self,card):
        if(self.num<13):
            self.hand_card_list.append(card)
            self.num+=1

    ## 定义整理手牌
    def arrange(self):
        self.hand_card_list.sort()

    ## 定义输出方便测试
    def __repr__(self):
        return (f"{self.hand_card_list}") ## 由于不能直接在__repr__里面返回

## 测试手牌类
if(False):
    card_1 = hand_card()
    cards=Poker()
    cards.shuffle()
    card_1.get_card(cards.deal())
    print(f"{card_1}")

## 定义玩家类
class Player():
    def __init__(self,name):
        self.name=name
        self.hand_card=[]

    def get_card(self,card):
        self.hand_card.append(card)

    ## 定义整理手牌
    def arrange(self):
        self.hand_card.sort() ## TypeError: '<' not supported between instances of 'Cards' and 'Cards'，需要重载“<”，由于是Cards类不能用<，因此
        # 重新定义一下Cards类里面的<，通过def __lt__即可。
    
    def __repr__(self):
        return f"{self.name}:{self.hand_card}"

## 主程序，创建手牌，创建牌堆，创建玩家，洗牌，发牌，把玩家和手牌连接
card_in_heap=Poker()
card_in_heap.shuffle()

players=[Player('东邪'), Player('西毒'), Player('南帝'), Player('北丐')]

for _ in range(12):
    for player in players:
        player.get_card(card_in_heap.deal())

for player in players:
    player.arrange()
    print(f'{player.name}: ', end='')
    print(player.hand_card)

# 执行上面的代码会在`player.arrange()`那里出现异常，因为`Player`的`arrange`方法使用了列表的`sort`对玩家手上的牌进行排序，
# 排序需要比较两个`Card`对象的大小，而`<`运算符又不能直接作用于`Card`类型，所以就出现了`TypeError`异常，异常消息为：
# `'<' not supported between instances of 'Card' and 'Card'`。

# 为了解决这个问题，我们可以对`Card`类的代码稍作修改，使得两个`Card`对象可以直接用`<`进行大小的比较。
# 这里用到技术叫**运算符重载**，Python中要实现对`<`运算符的重载，需要在类中添加一个名为`__lt__`的魔术方法。
# 很显然，魔术方法`__lt__`中的`lt`是英文单词“less than”的缩写，以此类推，
# 魔术方法`__gt__`对应`>`运算符，魔术方法`__le__`对应`<=`运算符，`__ge__`对应`>=`运算符，`__eq__`对应`==`运算符，`__ne__`对应`!=`运算符。

## eg2:工资结算系统
# 说明：某公司有三种类型的员工，分别是部门经理、程序员和销售员。需要设计一个工资结算系统，根据提供的员工信息来计算员工的月薪。
# 其中，部门经理的月薪是固定15000元；程序员按工作时间（以小时为单位）支付月薪，每小时200元；销售员的月薪由1800元底薪加上销售额5%的提成两部分构成。


# 通过对上述需求的分析，可以看出部门经理、程序员、销售员都是员工，有相同的属性和行为，那么我们可以先设计一个名为`Employee`的父类，
# 再通过继承的方式从这个父类派生出部门经理、程序员和销售员三个子类。
# 很显然，后续的代码不会创建`Employee` 类的对象，因为我们需要的是具体的员工对象，所以这个类可以设计成专门用于继承的抽象类。
# Python中没有定义抽象类的关键字，但是可以通过`abc`模块中名为`ABCMeta` 的元类来定义抽象类。

## 定义Employee元类（abc模块中的ABCMeta）
import abc

class Employee(metaclass=abc.ABCMeta):
    def __init__(self,name):
        self.name=name
    
    @abc.abstractmethod
    def get_salary(self):
        pass
# 在上面的员工类中，有一个名为`get_salary`的方法用于结算月薪，但是由于还没有确定是哪一类员工，所以结算月薪虽然是员工的公共行为但这里却没有办法实现。
# 对于暂时无法实现的方法，我们可以使用`abstractmethod`装饰器将其声明为抽象方法，抽象方法就是只有声明没有实现的方法，
# 声明这个方法是为了让子类去重写这个方法。接下来的代码展示了如何从员工类派生出部门经理、程序员、销售员这三个子类以及子类如何重写父类的抽象方法。

## 定义每一类员工
class Manager(Employee):
    def get_salary(self):
        return 15000

class Programmer(Employee):
    def __init__(self, name,working_hour=0):
        super().__init__(name) ## super()父类.__init__(name)父类定义的属性
        self.working_hour=working_hour
    
    def get_salary(self):
        return 200*self.working_hour

class Salesman(Employee):
    def __init__(self, name, sales=0):
        super().__init__(name)
        self.sales=sales

    def get_salary(self):
        return 1800+self.sales*0.05

# 上面的`Manager`、`Programmer`、`Salesman`三个类都继承自`Employee`，三个类都分别重写了`get_salary`方法。
# **重写就是子类对父类已有的方法重新做出实现**。相信大家已经注意到了，三个子类中的`get_salary`各不相同，
# 所以这个方法在程序运行时会产生**多态行为**，多态简单的说就是**调用相同的方法**，**不同的子类对象做不同的事情**。

# 我们通过下面的代码来完成这个工资结算系统，由于程序员和销售员需要分别录入本月的工作时间和销售额，
# 所以在下面的代码中我们使用了Python内置的`isinstance`函数来判断员工对象的类型。我们之前讲过的`type`函数也能识别对象的类型，
# 但是`isinstance`函数更加强大，因为它可以判断出一个对象是不是某个继承结构下的子类型，
# 可以简单的理解为`type`函数是对对象类型的精准匹配，而`isinstance`函数是对对象类型的模糊匹配。

emps = [
    Manager('刘备'), Programmer('诸葛亮'), Manager('曹操'), 
    Programmer('荀彧'), Salesman('吕布'), Programmer('张辽'),
]

for emp in emps:
    if isinstance(emp,Programmer):
        emp.working_hour = int(input(f'请输入{emp.name}本月工作时间: '))
    elif isinstance(emp,Salesman):
        emp.sales = float(input(f'请输入{emp.name}本月销售额: '))
    
    print(f'{emp.name}本月工资为: ￥{emp.get_salary():.2f}元')

# 简单总结：面向对象编程，重要的是：抽象，封装，继承，多态。其中还有装饰器，元类，抽象方法，枚举类型的用法，都需要慢慢积累。