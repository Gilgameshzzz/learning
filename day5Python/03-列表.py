"""
列表、字典、元组、集合都是序列，都是容器类型的数据类型

列表（list）：用来存储多个数据的一种数据类型。里面存储的单个数据，叫元素
特点1、有序的  2、可变的（可变指容器中的内容的个数和值可变）
3、元素可以是任何类型的数据
列表的值：用[]将列表中的元素括起来，多个元素之间用逗号隔开。[] -->空列表
"""
# 1、怎么声明一个列表
"""1、声明一个变量，赋一个列表值"""
list1 = []
print(type(list1))

"""2、将其他的数据类型转换成列表"""
list2 = list('police')
print(list2)

list3 = list(i*2 for i in range(10))
print(list3)

# 2、获取列表元素
# 列表中的每一个元素都对应一个下标：0~列表长度-1或-1~-列表长度
# a、获取单个元素：列表名[下标]
"""下标不能越界，会报IndexError"""
names = ['BMw', 'Audi', 'yuri', 'joe']
# b、获取部分元素（切片）
"""
列表名[起始下标：结束下标]：获取从起始下标开始，到结束下标前所有元素，结果是一个列表
列表名[起始下标：结束下标：步进]
起始下标和结束下标都可以缺省，
起始下标缺省如果步进为正，就从第一个开始取，如果步进是负数，就从最后一个开始取到结束下标
结束下标缺省，步进为正，获取到最后一个元素，步进是负数，从起始下标往前取到第一个元素
"""
print(names[:1:-1])
print(names[1::-1])
print(names[::-1])

print(names[:1])
print(names[1:])
print(names[:])
# 3、获取列表的长度（获取列表元素的个数）
"""
len（列表)
"""