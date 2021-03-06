# 1.注释
# (就是代码源文件中，用来进行注释说明的文字，不会对代码的功能产生任何影响）
# 注意：好的代码和好的程序员，需要对代码通过注释进行说明
# 单行注释

"""
这是多行注释
"""

'''
这是多行注释
'''
# 补充：编程语言中涉及到的所有的符号，都是指英文输入法状态下的符号

# 2.标识符
"""
标识符是用来程序中命名用的。（比如:变量名、类名、函数名）
a.标识符是由字母、数字和下划线组成并且数字不能开头（硬性要求）
---python3.X中，标识符里面可以有中文（但不推荐使用）
b.不能是关键字（保留字）（硬性要求）
c.大小写敏感（区分大小写，aaa和Aaa、AAA、AAa是不一样的）
d.要见名知义（规范）
e.不推荐使用Python中的内置函数、类名去作为标识符（规范）
"""
# 3.关键字
# 系统保留的有特殊功能或特殊意义的一些单词。这些单词不能用来给变量、函数、类等命名的
""" 
'False', 'None', 'True', 'and', 'as', 'assert', 'async',
 'await', 'break', 'class', 'continue', 'def', 'del', 
 'elif', 'else', 'except', 'finally', 'for', 'from', 'global',
  'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not',
   'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield'
"""
import keyword
print (keyword.kwlist)

# 4.行与缩进
"""
缩进：每一行代码的位置，与行头位置之间的空格
在Python中，缩进的写法有严格的规范。同一级的代码，必须在同一个缩进下面
如果在不该有空格产生的位置出现了多余的空格，程序会报错(IndentationError)；
如果在需要有缩进的时候没有缩进也会报错
关于行的规范：
函数和类的声明的前后必须要有两个换行。一般一个功能实现完，实现下一个功能
的时候，最好也换行。

"""
# 5.多行语句
"""
一条语句在多行显示。
a.在需要换行的地方加反斜杠（\）,然后再换行
b.字典、列表、集合和元组等容器类型数据的字面量，在多行显示的时候可以直接换行

Python中，一条语句结束，可以不写分号；但是如果一行中要写多条语句，那么每条
语句之间必须使用分号隔开

"""
# 6.字面量
# 数据类型对应的具体的值
"""
21,233,-21 --->整数
12.3,3.21232，-212.123 --->小数
12e3,33e-2 --->数字
3+23j --->复数
'dsad','2323','hello world','!ds31' --->字符串
True,False --->布尔
['dsa','dsaad','2112'] --->列表
{'ds':1,'axs':'212'} --->字典
。。。
"""

# 7.Python中的基本数据类型
# 数字（整型（int）、浮点型、布尔、复数）、字符串(str)、列表(list)、
# 字典(dict)、集合（set）、元组(tuple)、none --->代表没有和空
"""
整型 :int (在Python2.x中有long) ---->值是所有的整数
浮点型：float --->包含所有的小数,和科学计数
布尔 ：bool  --->值只有True和False
复数：complex --->值包含所有的复数
"""
# 可以type函数查看数据的类型：type（数据）



n = 6784
print( n / 1000 % 100 )
print(n % 1000 / 100)
print(n // 100 % 10)
print(n // 10  % 100 // 10)
 
 