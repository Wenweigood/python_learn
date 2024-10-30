# 根据缩进控制语法
import time

if True:
    print('True')

if 3 > 4:
    print('3>4')
else:
    print('3<4')
a = 5
if a < 5:
    print(a, '<', 5)
elif a > 5:
    print(a, '>', 5)
else:
    print(a, '=', 5)

# 短条件语句
# 通常条件和语句块比较简单的时候，也可以使用短语句形式（类比其他语言中的三目运算符）。
print('5<6' if 5 < 6 else '5>=6')

a = 15
if a < 100:
    print(a, '<100')
    if a < 50:
        print(a, '<50')
    else:
        print(a, '>50')
else:
    print(a, '>100')
if 5 > 2 and -1 < 2:
    print('5>2 and -1<2')

if 5 > 2 or -1 > 2:
    print('5>2 or -1>2')

print('------exercise------')
age = int(input("请输入你的年龄"))
if age >= 18:
    print("you can drive")
else:
    print('you can\'t drive')
age = int(input('我的年龄是25，请输入你的年龄'))
if age > 25:
    if age - 25 > 1:
        print('you are older than me', age - 25, 'years')
    else:
        print('you are older than me', age - 25, 'year')
elif age == 25:
    print('you have the same age with me')
else:
    if 25 - age > 1:
        print('you are younger than me', 25 - age, 'years')
    else:
        print('you are younger than me', 25 - age, 'year')

scores = int(input('input scores'))
if scores >= 80:
    print("A level")
elif scores >= 70:
    print("B level")
elif scores >= 60:
    print("C level")
elif scores >= 50:
    print('D level')
else:
    print('F level')

fruits = ['banana', 'orange', 'mango']
print('there are', fruits)
fruit = input('input fruit')
if fruit in fruits:
    print('already in list')
else:
    print('not in it')

person = {
    'name': 'MegaQi',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': ' 上海静安寺北京西路',
        'zipcode': '200041'
    }
}
if 'skills' in person.keys():
    print(person['skills'])
    if 'Python' in person['skills']:
        print('person can programing with Python')
    if len(person['skills']) == 2 and 'JavaScript' in person['skills'] and 'React' in person['skills']:
        print('front developer')
    elif ('Node' in person['skills'] and 'React' in person['skills']
          and 'MongoDB' in person['skills']):
        print('all skilled developer')
    elif ('Node' in person['skills'] and 'Python' in person['skills']
          and 'MongoDB' in person['skills']):
        print('backend developer')