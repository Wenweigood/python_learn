# 字典是有序（在3.6+以后从无序变有序的）、可修改可变、成对(key:value)的数据类型集合。
dct = dict({'1': 1, 2: 2})
print('dct.get(1)', dct.get(1))
print('dct.get(\'1\')', dct.get('1'))
print('dct.get(2)', dct.get(2))

# dct = {[1,2,3]:[123],1:1}
# print('dct.get([1,2,3])', dct.get([1,2,3]))
# 对dct的操作会导致 TypeError: unhashable type: 'list'

print(len(dct))
# 通过[]形式索引访问，如果对应key不存在，会抛出keyError
print(dct['1'])

# some examples
"""
person = {
    'name':'MegaQi',
    'age':100,
    'country':'China',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'Java', 'Python'],
    'address':{
        'city':'上海', 
        'street':'万航渡路'
    }
}
print(person['name'])       # MegaQi
print(person['country'])    # China
print(person['skills'])     # ['JavaScript', 'React', 'Node', 'Java', 'Python']
print(person['skills'][0])  # JavaScript
print(person['address']['street']) # 万航渡路
print(person['school'])       # KeyError: school
"""

# 增加字典
dct['none'] = 'a none value'
dct['list'] = [1, 2, 3]
dct['list'].append(6)
print(dct)

# 检查key
print('\'none\' in dct', 'none' in dct)

# 复制
dct2 = dct.copy()
print(dct2)

# 类型转换
dct3 = dct.items()
print(dct3)  # dict_items([('1', 1), (2, 2), ('none', 'a none value'), ('list', [1, 2, 3, 6])])

list1 = list(dct2)
print(list1)  # 只保留key

# 删除元素
dct2.pop('none')
# 删除最后一项
dct2.popitem()
del dct2['1']
print('deleted dct2', dct2)

# 清空
dct2.clear()

print('dct.keys()', dct.keys())
print('dct.values()', dct.values())

print('------exercise------')
dog = {}
dog['name'] = 'color'
dog['age'] = 'leg'
print('dog', dog)
student = {'name': 'wen', 'age': 25, 'skill': 'learning'}
print('len of student', len(student))
print('type of skill',type(student['skill']))
student['skill'] = ['c++','java','python']
print('keys of student', student.keys())
print('values of student', student.values())
print(student.items())
student.pop('name')
print(student)
del student
