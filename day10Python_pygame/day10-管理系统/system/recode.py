"""__author__ = 余婷"""
"""
1.模块
导入模块(自定义模块，第三方模块，系统其它模块)
import 模块  ---> 模块.内容
from 模块 import 内容 ---> 内容

被导入的模块中，除了声明在if __name__ == '__main__':判断中的内容以外的其他的全局的


2.文件操作
打开文件 -- 操作文件 -- 关闭文件
open() 操作文件 close() 
---> with open() as 文件:
        操作文件  
        
open(打开文件路径，打开方式-->'r'，编码方式-->二进制文件不能设置)  

文本文件  -> 'r'/'w','a'
二进制文件 -> 'rb'/'wb'
以读的形式打开文件，如果文件不存在会报错。以写的形式打开文件，如果文件不存在，会在指定的路径下创建该文件

read() --> 读文件中所有的内容
write() --> 将内容添加到文件中

3.json文件
json支持的数据类型和其对应的字面量
字符串(string) ---> ""
数字(number) ---> 10 / 12.9
布尔 ---> true/false
数组(array) ---> [12, "abc", true, "hhh"]
字典(object) ---> {"name":"abc", "age":10, "datas":[1, 2, 34, 89]}
null ---> null(空)  

import json
json.load(json文件对象) --> 读，读出来的数据的类型和json中对应的类型是一样的，可以读出字典、列表等数据
json.dump(要写入文件中的数据，json文件对象) --> 写，python中的基本数据类型，都可以直接写到json文件中  

4.异常捕获
try:
    需要捕获异常的代码（就是这段代码如果出现异常，不让程序崩溃）
except:
    只要try后面代码出现异常都会这行这段代码，并且程序不崩溃
    
    
try:
    需要捕获异常的代码块
except 异常类型：
    出现指定异常后才会执行
代码块3

try--except執行过程：先执行try后面的代码块，只要出现异常就使用except去捕获，如果能捕获到，就直接进入except中
                   执行里面的代码块，执行完成后，在执行后面的其他语句。如果捕获不到，就直接报错。如果try后面的代码
                   块中，没有异常。那么执行完代码块中的内容直接执行后面的其他语句
                   
想要同时捕获多个异常： except(错误类型1，错误类型2....):

try:
    代码块1
except:
    代码块2
finally:
    代码块3

try:
    代码块1
except 错误类型1：
    代码块2
except 错误类型2:
    代码块3

代码块3是在代码块1中没有出现异常，和代码1中出现异常被获取到都会执行


raise: 抛出异常


总结：1.异常捕获不是什么都要用，只有在程序员清楚会出现异常，并且想要自己来处理异常，而不是让程序崩溃的情况才异常捕获。
     2.使用异常捕获的时候，不能让except直接捕获所有的异常，而是捕获特定异常
"""

if __name__ == '__main__':

    try:
        # open('aaa.txt')
        print({'a': 'b', 'b': 1}['c'])
    except (IndexError, KeyError):
        print('出现异常')

    # print('异常捕获结束后')
    # finally:
    #     print('异常捕获结束后')
    while True:
        try:
            number = int(input('请输入数字：'))
            break
        except ValueError:
            print('输入有误！')

    print(number)





