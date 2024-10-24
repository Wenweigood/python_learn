"""
列表list：一个有序并且可修改的（可变）集合，允许有重复元素。
元组tuple：一个有序但不能改变或者修改的（不可变）集合，允许有重复元素。
集合set：一个无序，无索引且不可修改的集合。但可以向set中添加新的元素。不允许有重复元素。
字典dict：一个无序集合，可改变可修改，且有索引，没有重复元素。
"""

lst = list()
lst.append(1)
print(lst)

lst = [1, 2, {'a': '1', 'b': '2'}, (1, 5)]
print(lst)

# 拆包列表项
lst = ['item', 'item2', 'item3', 'item4', 'item5']
first_item, second_item, third_item, *rest = lst
print(first_item)  # item1
print(second_item)  # item2
print(third_item)  # item3
print(rest)  # ['item4', 'item5']

# 第一个例子：水果拆分前三项给1，2，3变量，剩余全部给rest
fruits = ['banana', 'orange', 'mango', 'lemon', 'lime', 'apple']
first_fruit, second_fruit, third_fruit, *rest = fruits
print(first_fruit)  # banana
print(second_fruit)  # orange
print(third_fruit)  # mango
print(rest)  # ['lemon','lime','apple']

# 第二个例子：前三项和最后一项分别给了对应变量，剩余所有中间组成一个集合给到rest
first, second, third, *rest, tenth = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(first)  # 1
print(second)  # 2
print(third)  # 3
print(rest)  # [4,5,6,7,8,9]
print(tenth)  # 10

# 判断某项是否存在list集合中使用 in 操作符。看如下例子：
fruits = ['banana', 'orange', 'mango', 'lemon']

print('banana' in fruits)  # True

print('lime' in fruits)  # False

print('lime' not in fruits)
fruits.append('lime')
print('lime' in fruits)
print(fruits)
fruits.insert(1, 123)
print(fruits)
# 移除指定元素
fruits.remove(123)  # 如果不存在会抛出异常
# 移除指定位置元素
fruits.pop(-1)
print(fruits)
# 删除元素或变量
del fruits[0]
print(fruits)
# 拷贝列表
fruits2 = fruits.copy()
print(fruits2)
# 清空列表
fruits.clear()
print(fruits)
# 连接list
print(fruits2 + [1, 2, 3, 4, 5])
fruits2.extend('12345')
print(fruits2)
# 统计出现次数
print(fruits2.count('3'))
print(fruits2.count(''))
# 查找指定项的索引
print(fruits2.index('lemon'))
# 排序
fruits2.sort(reverse=True)
print(fruits2)
fruits2.sort()
print(fruits2)
fruits3 = sorted(fruits2)  # 不改变原始列表的排序
print(fruits3)
print(sorted('132', reverse=True))
print('------exercise-----')
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
it_companies.append('Baidu')
it_companies[0] = it_companies[0].upper()
print('Google' in it_companies)
print(sorted(it_companies, reverse=True))
print(it_companies[-3:])
print(it_companies)
it_companies.pop(0)
it_companies.pop(int(len(it_companies) / 2))
print(it_companies)
it_companies.pop(-1)
it_companies.clear()
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']
front_end += back_end
print(front_end)
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print(ages)
print('max:', ages[-1], 'min:', ages[0])
print('middle:', ages[int(len(ages) / 2)])
count = 0
for age in ages:
    count += age
avg = count / len(ages)
print(avg)
print(abs(ages[0] - avg), abs(ages[-1] - avg))
c1,c2,c3, *other = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
print(c1)
print(c2)
print(c3)
print(other)
