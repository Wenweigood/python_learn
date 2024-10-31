# while
# for
c = 6
string = ''
while c > 0:
    c -= 1
    # print('c:', c)
    string += str(c)
print(string)
c = 6
string = ''
while c > 0:
    # print('c:', c)
    c -= 1
    if c == 2:
        break
    string += str(c)
print(string)
c = 6
string = ''
while c > 0:
    # print('c:', c)
    c -= 1
    if c == 2:
        continue
    string += str(c)
print(string)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in numbers:
    print(i)
string = 'wen vi !'
for s in string:
    print(s)
# 0 - 8, totally 9 symbols
for i in range(9):
    print(i, numbers)

person = {
    'name': 'MegaQi',
    'age': 180,
    'country': 'China',
    'is_marred': True,
    'skills': ['Java', 'React', 'Node', 'Mysql', 'Python']
}
for key in person:
    print(key)
for key, value in person.items():
    print(key, value)

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
for company in it_companies:
    # it will print items randomly
    print(company)
"""
范围函数 range
函数 range() 按给参数值返回一个数字列表。
函数 range(start, end, step) 有三个参数：开始、结束和增数。
默认情况下，它从0开始，增量为1。范围序列至少需要一个参数(end)。它将创建一个范围序列。
"""

for number in range(0, 20, 3):
    print(number)  # 打印0-10（不包含11）

person = {
    'name': 'MegaQi',
    'country': 'China',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'city': 'ShangHai',
        'code': '021'
    }
}
for key in person:
    if key == 'skills':
        for skill in person['skills']:
            print(skill)
    elif key == 'address':
        for address_key, address_value in person['address'].items():
            print(address_key, address_value)

# for else
# 如果我们想在循环结束时执行逻辑外代码则使用else。
for i in range(5):
    print(i)
else:
    print('print 5 numbers end')

# pass
# 在python中，语法冒号后必须要给定执行语句。但有时候我们不希望做任何事情。为了避免语法的错误，使用pass关键词做占位符。
# 只是一个占位符，不代表跳过
# 输出了寂寞
for number in range(6):
    pass
    print('print still works')

# 跳过4
for number in range(6):
    if number == 4:
        pass
    else:
        print(number)

print('------exercise------')
for i in range(7):
    string = ''
    for j in range(i + 1):
        string += '*'
    else:
        print(string)
for i in range(8):
    string = ''
    for j in range(8):
        string += '#'
    else:
        print(string)
for i in range(11):
    print('%d x %d = %d' % (i, i, i * i))