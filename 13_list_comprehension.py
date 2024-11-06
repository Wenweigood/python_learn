# 列表推导式
"""
# 语法形式
[i for i in iterable if expression]
它的结构是在一个中括号里包含一个表达式，然后是一个for语句，
然后是 0 个或多个 for 或者 if 语句。简单来讲，是从第一个for开始依次向右推导，
得出结果后给到最左边第一个变量。
"""

# 方式一
language = 'Python'
lst = list(language)  # 将字符串更改为list
print(type(lst))  # <type 'list'>
print(lst)  # ['P', 'y', 't', 'h', 'o', 'n']

# 方式二: 列表推导式
lst = [i for i in language]
print(type(lst))  # list
print(lst)  # ['P', 'y', 't', 'h', 'o', 'n']

lst = [i.upper() for i in language]
print(lst)

numbers = [i for i in range(100)]
print(numbers)

odds = [i for i in range(100) if i % 2 != 0]
print(odds)

# 将二维数组合并成一维数组
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list = [number for row in list_of_lists for number in row]
print(flattened_list)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# lambda函数
# 要创建lambda函数，我们使用 lambda 关键字后跟一个形参和表达式。Lambda函数不使用 return，它显式地返回表达式。

x = lambda p1, p2, p3: p1 + p2 + p3
print(x(1, 2, 3))
print(x('w', 'e', 'n'))


def power(x):
    return lambda n: x ** n


cube = power(2)(3)  # 函数power在括号需求两个参数来运行，参数先分配给x，然后分配给n
print(cube)  # 8
two_power_of_five = power(2)(5)
print(two_power_of_five)  # 32


def t_test(p1, p2):
    return lambda x, y, z: p1 * p2 + x * y * z


print(t_test(1, 2)(1, 2, 3))

print('------exercise------')

numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
numbers = [i for i in numbers if i >= 0]
print('numbers', numbers)

list_of_lists = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
list_of_lists = [i for j in list_of_lists for i in j]
print('list of list', list_of_lists)

tuples = [(i, 1, i, i * i, i * i * i, i * i * i * i, i * i * i * i * i) for i in range(11)]
for t in tuples:
    print(t)

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
countries = [[t[0][0].upper(),t[0][0][0:3].upper(),t[0][1].upper()] for t in countries]
print('countries', countries)

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
countries = [{'country':t[0].upper(),'city':t[1].upper()} for l in countries for t in l]
print('countries', countries)

names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]

names = [t[0]+' '+t[1] for l in names for t in l]
print('names', names)
