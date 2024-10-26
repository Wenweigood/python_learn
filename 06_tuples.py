# 元组
# 有序 & 不可变
"""
tuple()：创建一个空的元组
count()：计算元组中指定项的个数
index()：返回指定项的索引值
+ ：连接两个或以上的元组成为新的元组
"""
t1 = tuple((1, 2, 3))
print(t1)
print((4, 5, 6))

empty_tuple = ()
print(empty_tuple)

print(len(t1))

print(t1[0], t1[-1])
t2 = ("1", [1, 2, 3], (), (4, 5, 6))
l1 = ["1", [1, 2, 3], (), (4, 5, 6)]
print(t2)
print(l1)

print("-----separate-----")
print(t2[:])
print(t2[:2])
print(t2[2:])

# 元组、列表相互转换
l2 = list(t1)
t3 = tuple(l1)
print(l2)
print(t3)

print(1 in t1)
print(t1 + t2)
# 不能删除单个元组元素，但可以删除元组本身
del t1

print('------exercise------')
brothers = ('wen', 'wei', 'vi')
sisters = ('ww', 'vv')
siblings = brothers + sisters
print('len of siblings:', len(siblings))
family_members  = list(siblings)
family_members +=['father', 'mother']
family_members = tuple(family_members)
print('family', family_members)

siblings_split = family_members[:6]
parents_split = family_members[-2:]
print('siblings',siblings_split)
print('parents',parents_split)

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('is Estonia in nordic_countries:', 'Estonia' in nordic_countries)
print('is Iceland in nordic_countries:', 'Iceland' in nordic_countries)


