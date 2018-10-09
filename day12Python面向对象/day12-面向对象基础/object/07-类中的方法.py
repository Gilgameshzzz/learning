"""__author__ = 余婷"""
"""
属性: 对象的属性(属性)、类的属性(类的字段)
对象属性：属于对象的，不同对象对应的值可能不一样(对象属性，通过对象来使用)
类的字段: 声明在类里面，函数外面。类的属性属于类(类的字段，通过类来使用)

方法: 对象方法(方法)、类方法、静态函数
对象方法：自带一个self参数，一般要通过对象去调用
类方法：1.使用@classmethod修饰
       2.自带一个cls参数，并且这个参数不用传参，谁来调用这个方法，cls就指向谁
       3.类方法要通过类来调用
静态方法：1.使用@staticmethod修饰
        2.没有默认参数
        3.静态方法要通过类来调用
        
        
怎么选择用对象方法、类方法、静态方法？
if 如果实现函数的功能需要使用对象的属性，就声明成对象方法；

elif 如果实现函数的功能需要使用类的字段或者调用类的方法，就声明成类方法

else 如果实现函数功能既不需要对象的属性也不需要类的字段，就声明成静态方法


补充：ctr+r --> 查找替换
     ctr+f --> 查找
"""

class Person:
    # number是类字段
    number = 61

    def __init__(self, name='', age=0):
        # name 和 age是对象属性
        self.name = name
        self.age = age

    # eat方法是对象方法
    def eat(self, food):
        print('%s在吃%s' % (self.name, food))

    # hurt_earth就是一个类方法
    @classmethod
    def hurt_earth(cls):
        # cls指向的是调用这个方法的类，cls可以当成类来使用
        pt = cls('张三')  # 可以使用cls创建对象
        print(pt.name)

        print(cls.number)  # 可以通过cls使用类的字段

        print('人类破坏环境！！')

    # protect_earth是一个静态方法
    @staticmethod
    def protect_earth():
        pt = Person()
        print(Person.number)
        print('人类保护地球')



if __name__ == '__main__':
    # 1.类的字段要用类来使用
    print(Person.number)

    # 2.对象的属性要通过对象来使用
    p1 = Person('小明')
    print(p1.name, p1.age)

    # 3.对象方法用对象调用
    p1.eat('面条')

    p2 = Person('小红')
    p2.eat('火锅')

    # 4.类方法通过类来调用
    Person.hurt_earth()

    # 5. 静态方法通过类来调用
    Person.protect_earth()


"""
练习：
1.写一个班级类，属性：班级名、学生；功能：添加学生

2.写一个类，封装所有和数学运算相关的功能
"""


class Student:
    """学生类"""
    def __init__(self,name='', age=0):
        self.name = name
        self.age = age

    def __str__(self):
        return 'name:%s age:%d' % (self.name, self.age)

class Class:
    """班级类"""
    def __init__(self,name='', students=[]):
        self.class_name = name
        self.students = students

    def add_student(self):
        name = input('name:')
        age = input('age:')
        # 根据输入的信息创建学生对象
        stu = Student(name, int(age))
        # 添加学生
        # 列表中的元素可以是任何类型的数据
        self.students.append(stu)

# 创建班级类对象
cls1 = Class('py1805',[])

cls1.add_student()
students = cls1.students
stu = students[0]
print(stu.name)











