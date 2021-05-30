## 变量
"""
几种变量类型：int/float/str/bool/自定义
"""

## type 可以实现对于变量类型的判断，python是动态类型语言，不需要对于变量的提前类型定义

val_1 = "a"

print(type(val_1))

## 可以使用int()，float()，chr()，ord()实现类型的转换
## ord()实现ASCII码转换

print(ord(val_1))
## 97