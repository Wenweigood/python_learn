# 导入的模块名不能以数字开头
import string

import modules
import sys

# print(sys.argv[0], argv[1],sys.argv[2])
# 命令行执行将打印: 文件名 参数1 参数2
if len(sys.argv) >= 3:
    print('Welcome {}. Enjoy  {} challenge!'.format(sys.argv[1], sys.argv[2]))

# 导入时可以取别名
from modules import add_all as add, gravity as g

# 按此种方式导入后，也无需再加模块名前缀即可调用
from statistics import *

print(modules.gravity)
print(g)

print(modules.concat_with_space('w', 'v'))
print(add(1, 2))

print('python -V', sys.version)
print('sys.maxsize', sys.maxsize)

print(mean([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

import math

print('pi', math.pi)

print(string.punctuation)

from random import random, randint

print(random())  # 它返回一个介于0到0.9999之间的值
print(randint(5, 20))  # 它返回一个[5,20]的随机整数

print('------exercise------')

print(str(ord('a')))


def random_user_id():
    user_id = ''
    for i in range(6):
        p = randint(0, 35)
        if (p > 25):
            user_id += chr(p - 26 + ord('0'))
        else:
            user_id += chr(p + ord('a'))
    print('user_id', user_id)
    return user_id


random_user_id()


def random_user_id_by_user():
    l = int(input('input the length of user id:'))
    user_id = ''
    for i in range(l):
        p = randint(0, 35)
        if (p > 25):
            user_id += chr(p - 26 + ord('0'))
        else:
            user_id += chr(p + ord('a'))
    print('user_id', user_id)
    return user_id


random_user_id_by_user()


def list_of_hexa_colors():
    hexa = [0, 1, 2, 3, 4, 4, 5, 6, 7, 8, 9, 'a', 'b', 'c', 'd', 'e', 'f']
    result = '#'
    for i in range(6):
        result += str(hexa[randint(0, 15)])
    return result


print(list_of_hexa_colors())

def list_of_rgb_colors():
    return 'rgb(%d,%d,%d)'%(randint(0, 255), randint(0, 255), randint(0, 255))


print(list_of_rgb_colors())

def generate_colors(type='hexa', n=1):
    result = []
    if type == 'hexa':
        for i in range(n):
            result.append(list_of_hexa_colors())
    else:
        for i in range(n):
            result.append(list_of_rgb_colors())
    print(result)
    return result


generate_colors('hexa', 3) # ['#b0c6e9', '#c06ee9', '#871ff7']
generate_colors('hexa', 1) # ['#3b2366']
generate_colors('rgb', 3)  # ['rgb(85,243,216)', 'rgb(22,39,233)', 'rgb(235,151,123)']
generate_colors('rgb', 1)  # ['rgb(221,103,205)']