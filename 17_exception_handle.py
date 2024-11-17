"""
try:
    # 如果一切顺利，代码将在这里执行完毕
    code in this block if things go well
except:
    # 如果try代码出现错误将跳转到这里执行此处代码
    code in this block run if things go wrong
"""


def divide(a, b):
    return a / b


try:
    a = 1
    b = 0
    divide(a, b)
except:
    print(f'divide error,a:{a},b:{b}')

try:
    name = input('Enter your name:')
    year_born = input('Year you were born:')
    age = 2019 - year_born
    print(f'You are {name}. And your age is {age}.')
except TypeError:
    print('Type error occured')
except ValueError:
    print('Value error occured')
except ZeroDivisionError:
    print('zero division error occured')
# 没有异常时执行
else:
    print('else block')
# 无论是否有异常都执行 --与java一致
finally:
    print('finally block')

"""
* 表示任意数量的位置参数
** 表示任意数量的关键字参
"""


# 参数解包
def sum_of_five_nums(a, b, c, d, e):
    return a + b + c + d + e


lst = [1, 2, 3, 4, 5]
# 这里我理解为，像c++一样，使用*操作符从lst中取出元素（直接赋值由于类型list!=int不匹配会失败）
print(sum_of_five_nums(
    *lst))  # TypeError: sum_of_five_nums() missing 4 required positional arguments: 'b', 'c', 'd', and 'e'

# 列表或元组也可以像这样解包：
countries = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']
fin, sw, nor, *rest = countries  # *rest 将后两个国家打包成一个list
print(fin, sw, nor, rest)  # Finland Sweden Norway ['Denmark', 'Iceland']

numbers = [1, 2, 3, 4, 5, 6, 7]
one, *middle, last = numbers  # 前后两个赋值给前后两个变量，中间剩余全部打包成list
print(one, middle, last)  # 1 [2, 3, 4, 5, 6] 7


# 解压字典 dict
def unpacking_person_info(name, country, city, age):
    return f'{name} lives in {country}, {city}. He is {age} year old.'


dct = {'name': 'MegaQi', 'country': 'China', 'city': 'ShangHai', 'age': 18}
# 使用**关键字，使得从dct中获取入参时带上key，使用**操作符时，操作对象也必须为map
print(unpacking_person_info(**dct))  # MegaQi lives in China, ShangHai. He is 18 year old.


def print_multi_args(*args):
    print(args)


lst = ['w', 'vi']
print_multi_args(lst)


# 参数打包
# 打包列表参数
def sum_all(*args):
    s = 0
    for i in args:
        s += i
    return s


print(sum_all(1, 2, 3))  # 6
print(sum_all(1, 2, 3, 4, 5, 6, 7))  # 28


# 打包字典参数
def packing_person_info(**kwargs):
    for key in kwargs:
        print(f"{key} = {kwargs[key]}")
    return kwargs


print(packing_person_info(name="MegaQi", country="China", city="ShangHai", age=18))

# python的延展操作
# 这里使用*操作符实际上也是表示取其中元素，而非对象本身
lst_one = [1, 2, 3]
lst_two = [4, 5, 6, 7]
lst = [0, *lst_one, *lst_two]
print(lst)  # [0, 1, 2, 3, 4, 5, 6, 7]

country_lst_one = ['Finland', 'Sweden', 'Norway']
country_lst_two = ['Denmark', 'Iceland']
nordic_countries = [*country_lst_one, *country_lst_two]
print(nordic_countries)  # ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']

# 枚举
for index, item in enumerate([20, 30, 40]):
    print(index, item)

for index, item in enumerate({1:1,'w':'wen','vi':1}):
    print(index, item)

# 由于set是无序存储，这里每个元素的index可能会变
for index, item in enumerate({'a',1,2,'c'}):
    print(index, item)

# zip() 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表。
# 针对其中一个列表较长的，忽略其冗余元素
fruits = ['banana', 'orange', 'mango', 'lemon', 'lime']
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot','冗余']
zip_fruits_and_veges = zip(fruits, vegetables)
print(list(zip_fruits_and_veges))  # [('banana', 'Tomato'), ('orange', 'Potato'), ('mango', 'Cabbage'), ('lemon', 'Onion'), ('lime', 'Carrot')]

fruits_and_veges = []
for f, v in zip(fruits, vegetables):
    fruits_and_veges.append({'fruit':f, 'veg':v})

print(fruits_and_veges)

print('------exercise------')
names = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia']
*nordic_nations,es,ru = names

print('nordic_nations',nordic_nations)
print('es',es)
print('ru',ru)