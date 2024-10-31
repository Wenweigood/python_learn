#python中缩进用来表示代码块
"""
这是一
个
多行注释
"""
print("Hello world")

print(1+1)

print(True)

# 列表
# 所有类型均为数字
list1 = [0, 1, 2, 3, 4, 5]

# 所有项都是字符串类型（水果）
list2 = ['香蕉', '橙子', 'Mango']

# 混合类型，包括了字符、整数、布尔和浮点
list3 = ['芒果', 10, False, 9.81]

print(list1)

print(list3)

#字典 = map，k-v类型
dict1 = {
'name':'大奇',
'country':'中国',
'age':35,
'is_married':True,
'skills':['Python', 'React', 'Node', 'Java', 'Vue']
}

"""
元组tuple = enum
元组也是一个有序集合，但它不同于List。元组一旦创建就不能修改，它们是不可变的。
"""
#七大行星
tuple1 = ('地球', '木星', '海王星', '火星', '金星', '土星', '天王星', '水星')

#集合set，不重复元素
{2, 4, 3, 5}
{3.14, 9.81, 2.7} # 在set中顺序并不重要

print(type(list1))
print(type(dict1))
print(type(tuple1))

#计算两点距离 (2,3), (6,6)
p1 = (2,3)
p2 = (6,6)
print("(2,3), (6,6)的距离为：")
print(((p2[0] - p1[0])**2 + (p2[1]-p1[1])**2)**0.5)