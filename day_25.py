## day_25
## 用python读写CSV文件,excel文件

## CSV文件介绍
# CSV（Comma Separated Values）全称逗号分隔值文件是一种简单、通用的文件格式
# CSV是纯文本文件，不管是什么操作系统和编程语言都是可以处理纯文本，而且很多编程语言中都提供了对读写CSV文件的支持。

# CSV文件有以下特点：
# 1. 纯文本，使用某种字符集（如[ASCII](https://zh.wikipedia.org/wiki/ASCII)、[Unicode](https://zh.wikipedia.org/wiki/Unicode)、[GB2312](https://zh.wikipedia.org/wiki/GB2312)）等）；
# 2. 由一条条的记录组成（典型的是每行一条记录）；
# 3. 每条记录被分隔符（如逗号、分号、制表符等）分隔为字段（列）；
# 4. 每条记录都有同样的字段序列。

## 将数据写入CSV文件
# 说明：现有五个学生三门课程的考试成绩需要保存到一个CSV文件中，要达成这个目标
# 可以使用Python标准库中的`csv`模块，该模块的`writer`函数会返回一个`csvwriter`对象，
# 通过该对象的`writerow`或`writerows`方法就可以将数据写入到CSV文件中
import csv
import random

with open('scores.csv','w') as file: ## 打开文件，拥有写权限，命名为file
    writer = csv.writer(file) ## 调用写函数
    type(writer) ## csvwriter
    writer.writerow(['姓名', '语文', '数学', '英语'])
    names = ['关羽', '张飞', '赵云', '马超', '黄忠']
    for i in range(5):
        verbal = random.randint(50, 100)
        math = random.randint(40, 100)
        english = random.randint(30, 100)
        writer.writerow([names[i], verbal, math, english])
# note:需要说明的是上面的`writer`函数，该函数除了传入要写入数据的文件对象外，
# `dialect`参数，它表示CSV文件的方言，默认值是`excel`。
# 可以通过`delimiter`、`quotechar`、`quoting`参数来指定分隔符（默认是逗号）、包围值的字符（默认是双引号）以及包围的方式。
# 其中，包围值的字符主要用于当字段中有特殊符号时，通过添加包围值的字符可以避免二义性。
# 大家可以尝试将上面第5行代码修改为下面的代码，看看生成的CSV文件到底有什么区别。
writer = csv.writer(file, delimiter='|', quoting=csv.QUOTE_ALL)

## 读取csv文件数据
# 读取CSV文件，可以通过`csv`模块的`reader`函数可以创建出`csvreader`对象，该对象是一个迭代器，可以通过`next`函数或`for-in`循环读取到文件中的数据。
import csv

with open('scores.csv', 'r') as file:
    reader = csv.reader(file, delimiter='|')
    for line in reader:
        print(reader.line_num, end='\t')
        for elem in line:
            print(elem, end='\t')
        print()
## note：上面的代码对`csvreader`对象做`for`循环时，每次会取出一个列表对象，该列表对象包含了一行中所有的字段。

## 总结：csv这个Python标准库其实不是特别好用，之后还是得用pandas这个库，功能比较强大
# `pandas`中封装了名为`read_csv`和`to_csv`的函数用来读写CSV文件，其中`read_CSV`会将读取到的数据变成一个`DataFrame`对象，
# 而这个对象就是`pandas`库中最重要的类，它封装了一系列的方法用于对数据进行处理（清洗、转换、聚合等）；
# 而`to_csv`会将`DataFrame`对象中的数据写入CSV文件，完成数据的持久化。

## 用Python读写Excel文件
# Python操作Excel需要三方库的支持，如果要兼容`xls`格式的Excel文件，可以使用三方库`xlrd`和`xlwt`，前者用于读Excel文件，后者用于写Excel文件。
# 如果操作`xlsx`格式的Excel文件，也可以使用`openpyxl`库，当然这个库不仅仅可以操作Excel，还可以操作其他基于Office Open XML的电子表格文件。

## `xlwt`和`xlrd`为例讲解如何读写Excel文件
## 安装这两个库：pip install xlwt xlrd -i https://pypi.doubanio.com/simple

## 读.xls文件
import xlrd

# 使用xlrd模块的open_workbook函数打开指定Excel文件并获得Book对象（工作簿）
wb = xlrd.open_workbook('阿里巴巴2017年股票数据.xlsx')
# 通过Book对象的sheet_names方法可以获取所有表单名称
sheetname = wb.sheet_names()[0]
# 通过指定的表单名称获取Sheet对象（工作表）
sheet = wb.sheet_by_name(sheetname)
# 通过Sheet对象的nrows和ncols属性获取表单的行数和列数
print(sheet.nrows, sheet.ncols)
for row in range(sheet.nrows):
    for col in range(sheet.ncols):
        # 通过Sheet对象的cell方法获取指定Cell对象（单元格）
        # 通过Cell对象的value属性获取单元格中的值
        value = sheet.cell(row, col).value
        # 对除首行外的其他行进行数据格式化处理
        if row > 0:
            # 第1列的xldate类型先转成元组再格式化为“年月日”的格式
            if col == 0:
                # xldate_as_tuple函数的第二个参数只有0和1两个取值
                # 其中0代表以1900-01-01为基准的日期，1代表以1904-01-01为基准的日期
                value = xlrd.xldate_as_tuple(value, 0)
                value = f'{value[0]}年{value[1]:>02d}月{value[2]:>02d}日'
            # 其他列的number类型处理成小数点后保留两位有效数字的浮点数
            else:
                value = f'{value:.2f}'
        print(value, end='\t')
    print()
# 获取最后一个单元格的数据类型
# 0 - 空值，1 - 字符串，2 - 数字，3 - 日期，4 - 布尔，5 - 错误
last_cell_type = sheet.cell_type(sheet.nrows - 1, sheet.ncols - 1)
print(last_cell_type)
# 获取第一行的值（列表）
print(sheet.row_values(0))
# 获取指定行指定列范围的数据（列表）
# 第一个参数代表行索引，第二个和第三个参数代表列的开始（含）和结束（不含）索引
print(sheet.row_slice(3, 0, 5))

## 更多关于`xlrd`模块的知识，可以阅读它的官方文档(https://xlrd.readthedocs.io/en/latest/)。

## 写.xls文件
# 写入Excel文件可以通过`xlwt` 模块的`Workbook`类创建工作簿对象，通过工作簿对象的`add_sheet`方法可以添加工作表，
# 通过工作表对象的`write`方法可以向指定单元格中写入数据，
# 最后通过工作簿对象的`save`方法将工作簿写入到指定的文件或内存中。下面的代码实现了将5个学生3门课程的考试成绩写入Excel文件的操作。
import random
import xlwt

student_names = ['关羽', '张飞', '赵云', '马超', '黄忠']
scores = [[random.randint(40, 100) for _ in range(3)] for _ in range(5)]
# 创建工作簿对象（Workbook）
wb = xlwt.Workbook()
# 创建工作表对象（Worksheet）
sheet = wb.add_sheet('一年级二班')
# 添加表头数据
titles = ('姓名', '语文', '数学', '英语')
for index, title in enumerate(titles):
    sheet.write(0, index, title)
# 将学生姓名和考试成绩写入单元格
for row in range(len(scores)):
    sheet.write(row + 1, 0, student_names[row])
    for col in range(len(scores[row])):
        sheet.write(row + 1, col + 1, scores[row][col])
# 保存Excel工作簿
wb.save('考试成绩表.xlsx')

## 调整单元格样式
# 可以为单元格设置样式，主要包括字体（Font）、对齐方式（Alignment）、边框（Border）和背景（Background）的设置，`xlwt`对这几项设置都封装了对应的类来支持。
# 要设置单元格样式需要首先创建一个`XFStyle`对象，再通过该对象的属性对字体、对齐方式、边框等进行设定，
# 例如在上面的例子中，如果希望将表头单元格的背景色修改为黄色，可以按照如下的方式进行操作
header_style = xlwt.XFStyle()
pattern = xlwt.Pattern()
pattern.pattern = xlwt.Pattern.SOLID_PATTERN
# 0 - 黑色、1 - 白色、2 - 红色、3 - 绿色、4 - 蓝色、5 - 黄色、6 - 粉色、7 - 青色
pattern.pattern_fore_colour = 5
header_style.pattern = pattern
titles = ('姓名', '语文', '数学', '英语')
for index, title in enumerate(titles):
    sheet.write(0, index, title, header_style)

## 如果希望为表头设置指定的字体，可以使用`Font`类并添加如下所示的代码。
font = xlwt.Font()
# 字体名称
font.name = '华文楷体'
# 字体大小（20是基准单位，18表示18px）
font.height = 20 * 18
# 是否使用粗体
font.bold = True
# 是否使用斜体
font.italic = False
# 字体颜色
font.colour_index = 1
header_style.font = font

## 如果希望表头垂直居中对齐，可以使用下面的代码进行设置。
align = xlwt.Alignment()
# 垂直方向的对齐方式
align.vert = xlwt.Alignment.VERT_CENTER
# 水平方向的对齐方式
align.horz = xlwt.Alignment.HORZ_CENTER
header_style.alignment = align

## 如果希望给表头加上黄色的虚线边框，可以使用下面的代码来设置。
borders = xlwt.Borders()
props = (
    ('top', 'top_colour'), ('right', 'right_colour'),
    ('bottom', 'bottom_colour'), ('left', 'left_colour')
)
# 通过循环对四个方向的边框样式及颜色进行设定
for position, color in props:
    setattr(borders, position, xlwt.Borders.DASHED)
    setattr(borders, color, 5)
header_style.borders = borders

## 如果要调整单元格的宽度（列宽）和表头的高度（行高），可以按照下面的代码进行操作。
# 设置行高为40px
sheet.row(0).set_style(xlwt.easyxf(f'font:height {20 * 40}'))
titles = ('姓名', '语文', '数学', '英语')
for index, title in enumerate(titles):
    # 设置列宽为200px
    sheet.col(index).width = 20 * 200
    # 设置单元格的数据和样式
    sheet.write(0, index, title, header_style)

## 公式计算（对前面打开的那个文件进行操作）
# 要统计全年收盘价（Close字段）的平均值以及全年交易量（Volume字段）的总和，可以使用Excel的公式计算即可。我们可以先使用`xlrd`读取Excel文件夹，
# 然后通过一个名为`xlutils`的三方库提供的`copy`函数将读取到的Excel文件转成`Workbook`对象进行写操作，在调用`write`方法时，可以将一个`Formula`对象写入单元格。
# pip install xlutils -i https://pypi.doubanio.com/simple ## 安装xlutils库

## 实现公式计算的代码如下所示。
import xlrd
import xlwt
from xlutils.copy import copy

wb_for_read = xlrd.open_workbook('阿里巴巴2017年股票数据.xlsx')
sheet1 = wb_for_read.sheet_by_index(0)
nrows, ncols = sheet1.nrows, sheet1.ncols
wb_for_write = copy(wb_for_read)
sheet2 = wb_for_write.get_sheet(0)
sheet2.write(nrows, 4, xlwt.Formula(f'average(E2:E{nrows})'))
sheet2.write(nrows, 6, xlwt.Formula(f'sum(G2:G{nrows})'))
wb_for_write.save('阿里巴巴2017年股票数据-2.xlsx')

## 总结：其他操作Excel文件的三方库（如`openpyxl`）大家有兴趣可以自行了解。
# 掌握了Python程序操作Excel的方法，可以解决日常办公中很多繁琐的处理Excel电子表格工作，
# 最常见就是将多个数据格式相同的Excel文件合并到一个文件以及从多个Excel文件或表单中提取指定的数据。
#
# 如果要对表格数据进行处理，使用Python数据分析神器之一的`pandas`库可能更为方便，因为`pandas`库封装的函数以及`DataFrame`类可以完成大多数数据处理的任务。
#
# 本章例子中使用的Excel文件，大家可以从百度云盘链接中进行下载，地址：<https://pan.baidu.com/s/1rQujl5RQn9R7PadB2Z5g_g>，提取码：e7b4。
