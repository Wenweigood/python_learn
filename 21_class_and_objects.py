"""
Python是一种面向对象的编程语言。
Python中的所有东西都是一个对象，包括它的属性和方法。
程序中使用的数字、字符串、列表、字典、元组、集合等都是相应内置类对象。我们创建类来创建对象。
类，类似于对象构造函数，或者创建对象的“蓝图”。
我们实例化一个类来创建一个对象。
类定义对象的属性和行为，而另一方面，对象表示类。
"""
import math


# 要创建一个类，我们需要使用关键词 class 然后后边跟着名字和冒号，类的名字建议使用驼峰命名法


class Person:
    # 属于类的变量，而不属于实例，类似于java的static
    species = "human"

    # python函数形参允许带默认值，约束应该也类似c++
    def __init__(self, name, age, country="china"):
        # 定义在构造函数的变量才属于示例
        self.name = name
        self.age = age
        self.country = country

    def print_age(self):
        print('name:{}, age:{}'.format(self.name, self.age))
        print('name:%s, age:%d' % (self.name, self.age))
        print(f'name:{self.name}, age:{self.age}')

    def add_skill(self, skill):
        # hasattr用于检查类是否有某个属性
        if (not hasattr(self, 'skill')):
            self.skill = []
        self.skill.append(skill)


print(Person)

p = Person('wen', 26)

print(p)  # <__main__.Person object at 0x000002084C138490>
print(p.age)
p.print_age()
print(Person.species)
print(p.species)

p.add_skill('drawing')
p.add_skill('swimming')

print("p.skill:", p.skill)


# python继承
# 括号内可写多个类，说明是多继承
class Student(Person):
    def __init__(self, score=0):
        # 通过super()调用父类构造函数 或其他属性，这一点类似java
        super().__init__(age=10, name='vi')
        self.score = score

    #重写父类方法
    def add_skill(self, skill):
        if(not hasattr(self,'skill')):
            self.skill = []
        self.skill.append(skill.upper())


s1 = Student()

s1.add_skill('learning')

print('s1.skill:', s1.skill)


print('------exercise------')

class Statistics:
    def __init__(self):
        self.samples = []

    def add_number(self, o):
        self.samples.append(o)
    def add_numbers(self, l):
        self.samples.extend(l)

    def avg(self):
        count = 0
        for i in self.samples:
            count += i
        return count/len(self.samples)

    def middle(self):
        self.samples.sort()
        return self.samples[int(len(self.samples)/2)]

    def sigma(self):
        count = 0
        for i in self.samples:
            count += i*i
        return math.sqrt(count)

s1 = Statistics()
s1.add_numbers([1,2,3,4,5])

print(s1.samples,'avg',s1.avg())
print(s1.samples,'middle',s1.middle())
print(s1.samples,'sigma',s1.sigma())
