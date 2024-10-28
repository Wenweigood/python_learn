set1 = {1,2,3,'1','wen'}
set2 = set([2,3,4])
print('set1',set1)
print('len of set2',len(set2))

print('\'wen\' in set1','wen' in set1)

# Set一旦被创建，内部的项是不可以改变的。但是我们可以向其添加新项。
set1.add('vi')
print(set1)

# 使用 update() 添加多个项，函数参数是一个list。
st = {'item1', 'item2', 'item3', 'item4'}
st.update(['item5','item6','item7'])
print(st)

print(set1)
# 移除项，如果不存在会报错
set1.remove('wen')
print(set1)
# 移除项，但即便不存在也不报错
set1.discard('wen')
print(set1)

# 移除随机的项
poped = set1.pop()
print('poped:', poped)

set1.clear()

del set1

# 我们可以在list和set之间相互转换。将list转set的时候会移除重复项，仅有唯一值将被保留。
l = [1,2,4,4,6]
s = {'wen','wei','vi'}
print('set(l)',set(l))
print('list(s)',list(s))

# 连接set使用 union或者update
union_set = s.union(set(l))
print('union_set',union_set)
s.update(set(l))
print('s',s)

inter = s.intersection(set(l))
print(inter)

differ = s.difference(set(l))
print(differ)

# 判断超集issuperset()、子集issubset()

"""
如果两个集合没有一个或多个共同项，我们称它们为不相交集。
我们可以使用 isdisjoint() 方法检查两个集合是连接的还是不连接的。
或者可理解为用于判断两个集合是否包含相同的元素，如果没有返回 True，否则返回 False。
"""
print(s.isdisjoint(l))

print('------exercise------')
# 已知有如下集合set
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
print('len of it_companies:', len(it_companies))
it_companies.add('Twitter')
it_companies.update({'telegram', 'openAI'})
print('it_companies:',it_companies)
it_companies.remove('Google')

C = A.union(B)
inter = A.intersection(B)
print('inter', inter)
print('A.issubset(B)', A.issubset(B))
print('是否有相同元素：', not A.isdisjoint(B))
inter1, inter2 = A.union(B), B.union(A)
print(inter1)
print(inter2)
del A, B
print('len of list age',len(age),'len of set age',len(set(age)))
