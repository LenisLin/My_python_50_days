## day_22
## 对象的序列化和反序列化

## 读写JSON格式的数据
# 通过上面的讲解，我们已经知道如何将文本数据和二进制数据保存到文件中，那么这里还有一个问题，如果希望把一个列表或者一个字典中的数据保存到文件中又该怎么做呢？

# 在Python中，我们可以将程序中的数据以JSON格式进行保存。
# JSON是“JavaScript Object Notation”的缩写，它本来是JavaScript语言中创建对象的一种字面量语法，现在已经被广泛的应用于跨语言跨平台的数据交换。
# 使用JSON的原因非常简单，因为它结构紧凑而且是纯文本，任何操作系统和编程语言都能处理纯文本，这就是实现跨语言跨平台数据交换的前提条件。
#
# 目前JSON基本上已经取代了XML（可扩展标记语言）作为异构系统间交换数据的事实标准。
# 可以在[JSON的官方网站](https://www.json.org/json-zh.html)找到更多关于JSON的知识，这个网站还提供了每种语言处理JSON数据格式可以使用的工具或三方库。

# 在R语言中，我用rjson包来便捷处理.json文件

## JSON格式文件举例
{
    "name": "骆昊",
    "age": 40,
    "friends": ["王大锤", "白元芳"],
    "cars": [
        {"brand": "BMW", "max_speed": 240},
        {"brand": "Benz", "max_speed": 280},
        {"brand": "Audi", "max_speed": 280}
    ]
}
## 跟Python中的字典非常类似而且支持嵌套结构，就像Python字典中的值还可以是字典，如果我们把下面的代码输入到浏览器控制台中（打开浏览器点F12），它会创建出一个JavaScript中的对象。

## JSON格式的数据类型和Python的数据类型对应关系
# | Python                                 | JSON         |
# | -------------------------------------- | ------------ |
# | dict                                   | object       |
# | list, tuple                            | array        |
# | str                                    | string       |
# | int, float, int- & float-derived Enums | number       |
# | True / False                           | true / false |
# | None                                   | null         |

## Python中，我们可以使用`json`模块将字典或列表以JSON格式写入到文件中
import json

my_dict = {
    'name': '骆昊',
    'age': 40,
    'friends': ['王大锤', '白元芳'],
    'cars': [
        {'brand': 'BMW', 'max_speed': 240},
        {'brand': 'Audi', 'max_speed': 280},
        {'brand': 'Benz', 'max_speed': 280}
    ]
}
with open('data.json','w') as file: ## 原来没有data.json这个文件
    json.dump(my_dict,file)
print('字典已经保存到data.json文件中')
# 执行上面的代码，在此时的工作目录下面会创建`data.json`文件，文件的内容如下所示，中文是用Unicode编码书写的。

## json模块的重要函数
# - `dump` - 将Python对象按照JSON格式序列化到文件中
# - `dumps` - 将Python对象处理成JSON格式的字符串
# - `load` - 将文件中的JSON数据反序列化成对象
# - `loads` - 将字符串的内容反序列化成Python对象

## 序列化 & 反序列化
# [维基百科]解释：
# “序列化（serialization）在计算机科学的数据处理中，是指将数据结构或对象状态转换为**可以存储或传输的形式**，
# 这样在需要的时候能够恢复到原先的状态，而且通过序列化的数据重新获取字节时，可以利用这些字节来产生原始对象的副本（拷贝）。

# 与这个过程相反的动作，即从一系列字节中提取数据结构的操作，就是反序列化（deserialization）”

## 从上面创建的`data.json`文件中读取JSON格式的数据并还原成字典
import json
with open('data.json','r') as file:
    re_my_dict_=json.load(file) ## load，从json文件中反序列化为对象
    print(re_my_dict_)
    print(my_dict)

## 包管理工具 pip
# Python标准库中的`json`模块在数据序列化和反序列化时性能并不是非常理想，为了解决这个问题，可以使用三方库`ujson`来替换`json`。
# 所谓三方库，是指非公司内部开发和使用的，也不是来自于官方标准库的Python模块，这些模块通常由其他公司、组织或个人开发，所以被称为三方库。
# 就是类似R语言很多别人写的R包

# 之前安装Python解释器时，默认情况下已经勾选了安装pip，大家可以在命令提示符或终端中通过`pip --version`来确定是否已经拥有了pip。
# pip是Python的包管理工具，通过pip可以查找、安装、卸载、更新Python的三方库或工具，macOS和Linux系统应该使用pip3。
# 例如要安装替代`json`模块的`ujson`，可以使用下面的命令。pip install ujson ## bash命令

# 在默认情况下，pip会访问`https://pypi.org/simple/`来获得三方库相关的数据，但是国内访问这个网站的速度并不是十分理想，
# 因此国内用户可以使用豆瓣网提供的镜像来替代这个默认的下载源，操作如下所示。
pip install ujson -i https://pypi.doubanio.com/simple ## -i指定下载镜像

# 可以通过`pip search`命令根据名字查找需要的三方库，可以通过`pip list`命令来查看已经安装过的三方库。
# 如果想更新某个三方库，可以使用`pip install -U`或`pip install --upgrade`；如果要删除某个三方库，可以使用`pip uninstall`命令。
pip search ujson ## 搜索库
pip install ujson ## 安装库
pip install --update ## 更新库
pip uninstall ## 删除库
pip list ## 查看已有的库

## 更新Pip本身
python -m pip install -U pip ## Windows
pip3 install -U pip ## MAC and Linux

## 使用网络API获取数据
# 如果想在我们自己的程序中显示天气、路况、航班等信息，这些信息我们自己没有能力提供，所以必须使用网络数据服务。
# 目前绝大多数的网络数据服务（或称之为网络API）都是基于HTTP提供JSON格式的数据。
# 在Python程序中，我们可以发送HTTP请求给指定的URL（统一资源定位符），这个URL就是所谓的网络API，
# 如果请求成功，它会返回HTTP响应，而HTTP响应的消息体中就有我们需要的JSON格式的数据。
# 关于HTTP的相关知识，可以看看阮一峰的[《HTTP协议入门》](http://www.ruanyifeng.com/blog/2016/08/http.html)一文。
#
# 国内有很多提供网络API接口的网站，例如[聚合数据](https://www.juhe.cn/)、[阿凡达数据](http://www.avatardata.cn/)等，
# 这些网站上有免费的和付费的数据接口，国外的[{API}Search](http://apis.io/)网站也提供了类似的功能，有兴趣的可以自行研究。
# 下面演示如何使用[`requests`]库（基于HTTP进行网络资源访问的三方库）访问网络API获取内容，
# 这个例子使用了[天行数据](https://www.tianapi.com/)提供的数据接口，其中的APIKey需要自己到网站上注册申请。

## 安装requests库并加载
pip install requests
import requests

## 获取内容。
resp = requests.get('http://api.tianapi.com/txapi/caihongpi/index?key=ecc75528e8444a8265069fe484c22997')
if resp.status_code == 200:
    data_model = resp.json()
    for content in data_model['newslist']:
        print(content['content'])
    # 注意：上面代码中的APIKey需要换成自己在天行数据网站申请的APIKey，同时还要申请开通国内新闻的接口才能获取到JSON格式的数据。
    # 这个网站上还有很多非常有意思的网络API接口，例如：垃圾分类、美女图片、周公解梦等等，大家可以仿照上面的代码来调用这些接口。

## 总结：
# Python中实现序列化和反序列化除了使用`json`模块之外，还可以使用`pickle`和`shelve`模块，
# 但是这两个模块是使用特有的序列化协议来序列化数据，因此序列化后的数据只能被Python识别，关于这两个模块的相关知识可以自己看看网络上的资料。
# 处理JSON格式的数据很显然是程序员必须掌握的一项技能，因为不管是访问网络API接口还是提供网络API接口给他人使用，都需要具备处理JSON格式数据的相关知识。