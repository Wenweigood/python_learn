"""
一个函数可以被作为另一个函数的一或多个参数
一个函数可以被作为结果或另一个函数返回
一个函数可以被修改
一个函数可以赋值给一个变量
"""
import os


# 函数作为参数
def sum_numbers(nums):  # 正常函数
    return sum(nums)  # 利用内置函数返回列表和


def higher_order_function(f, lst):  # 高阶函数：函数作为另一个函数其中一个参数
    summation = f(lst)
    return summation


result = higher_order_function(sum_numbers, [1, 2, 3, 4, 5])
print(result)  # 15


# 函数作为返回值
def square(x):  # 平方函数
    return x ** 2


def cube(x):  # 立方函数
    return x ** 3


def absolute(x):  # 绝对值函数
    if x >= 0:
        return x
    else:
        return -(x)


def higher_order_function(type):  # 将函数作为返回值，声明一个高阶函数
    if type == 'square':
        return square
    elif type == 'cube':
        return cube
    elif type == 'absolute':
        return absolute


result = higher_order_function('square')
print(result(3))  # 9
result = higher_order_function('cube')
print(result(3))  # 27
result = higher_order_function('absolute')
print(result(-3))  # 3
print(type(result))  # <class 'function'>

"""
Python允许嵌套一个函数，此函数可以访问外部函数的变量。这就是所谓的闭包。
让我们看看闭包在Python中是如何工作的。在Python中，闭包是通过在另一个封装函数中嵌套一个函数，然后返回内部函数来创建的。
"""

a = 10


def times_a_fixed_number(m):
    b = 10

    def inner_functions(n):
        return n * m * a * b

    return inner_functions


a_hundred_times = times_a_fixed_number(100)

print(a_hundred_times(5))  # 50000
a = 1
print(a_hundred_times(5))  # 5000
"""
闭包在Python中的作用：
1、读取函数内部的变量
2、让函数内部的局部变量始终保持在内存中
"""


# 正常写法
def greeting():
    return 'Welcome to Python'


def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase

    return wrapper


greeting = uppercase_decorator(greeting)
print(greeting())  # WELCOME TO PYTHON

# 用一个装饰器来实现上面的例子
'''这个装饰函数，它是一个高阶函数，它以一个函数作为参数'''


def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase

    return wrapper


@uppercase_decorator  # 通过@注解
def greeting():
    return 'Welcome to Python'


print(greeting())  # WELCOME TO PYTHON

'''这个装饰函数，它是一个高阶函数，
它以一个函数作为参数'''


# 多装饰器
# 第一个装饰器：字符转大写
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase

    return wrapper


# 第二个装饰器：拆分字符串
def split_string_decorator(function):
    def wrapper():
        func = function()
        splitted_string = func.split()
        return splitted_string

    return wrapper


@split_string_decorator
@uppercase_decorator  # 这里注意多个装饰的执行顺序：先执行在底部，这里为先转大写再拆分
def greeting():
    return 'Welcome to Python'


print(greeting())  # ['WELCOME', 'TO', 'PYTHON']


# 装饰器带参数
def decorator_with_parameters(function):
    def wrapper_accepting_parameters(para1, para2, para3):
        # 首先调用原函数
        function(para1, para2, para3)
        # 其次调用装饰的逻辑
        print("I live in {}".format(para3))

    return wrapper_accepting_parameters


@decorator_with_parameters
def print_full_name(first_name, last_name, country):
    print("I am {} {}. I love to teach.".format(
        first_name, last_name, country))


print_full_name("Mega", "Qi", 'China')

# 内置高阶函数
# map() 函数是一个内置函数，它以函数和可迭代对象作为参数。
# 语法形式
# map(function, iterable)

numbers = [1, 2, 3, 4, 5]  # iterable


def square(x):
    return x ** 2


numbers_squared = map(square, numbers)
print(list(numbers_squared))  # [1, 4, 9, 16, 25]

# 让我们将它应用到 lambda 匿名函数上
numbers_squared = map(lambda x: x ** 2, numbers)
print(list(numbers_squared))  # [1, 4, 9, 16, 25]

numbers_str = ['1', '2', '3', '4', '5']  # iterable
numbers_int = map(int, numbers_str)  # 将字符串列表迭代转成数字列表
print(list(numbers_int))  # [1, 2, 3, 4, 5]

# 实际 map 做的事情是迭代一个列表

# 函数 filter() 调用指定的函数，该函数为指定的可迭代对象(列表)的每一项布尔值返回。即它过滤满足条件的项。
# 语法形式
# filter(function, iterable)

numbers = [i for i in range(10)]
print('numbers:', numbers)

odd_only = filter(lambda i: i % 2 == 0, numbers)
print('odd_only:', list(odd_only))

# Lets filter only even nubers
numbers = [1, 2, 3, 4, 5]  # iterable

names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']  # iterable


def is_name_long(name):
    if len(name) > 7:
        return True
    return False


long_names = filter(is_name_long, names)
print(list(long_names))  # ['Asabeneh']

# 函数 reduce() 会对参数序列中元素进行累积。
# 是在 functools 模块中定义的。我们要使用它需要从这个模块中导入。
# 像map和filter一样，它有两个参数，一个函数参数和一个可迭代对象参数。
# 但它不会返回另一个迭代对象，而是返回一个单独的值。

from functools import *

added = reduce(lambda x, y: x + y, numbers)
print('added:', added)

print('------exercise------')
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for c in countries:
    print(c)
for n in names:
    print(n)
for n in numbers:
    print(n)

upper_case_countries = map(lambda x: x.upper(), countries)
print('upper_case_countries:', list(upper_case_countries))

powered = map(lambda x: x ** 2, numbers)
print('powered:', list(powered))

filter_land = filter(lambda x: 'land' not in x, countries)
print('filter_land:', list(filter_land))

filter_e_at_first = filter(lambda x: x.startswith('E'), countries)
print('filter_e_at_first:', list(filter_e_at_first))

reduced_countries = reduce(lambda x, y: x + '、' + y, countries)
reduced_countries += '都是北欧国家'
print('reduced_countries:', reduced_countries)

from data.countries import countries

sorted_by_name = sorted(countries, key = lambda x: x['name'])
print(sorted_by_name)

sorted_by_capital = sorted(countries, key = lambda x: x['capital'])
print(sorted_by_capital)

sorted_by_population = sorted(countries, key = lambda x: x['population'])
print(sorted_by_population)

print('ten largest population countries in countries.py:\n',list(map(lambda x:x['name'],sorted_by_population[-10:])))
