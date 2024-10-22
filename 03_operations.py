print(1 >= 2)
print(1 >= 1)

# 以下实例都将返回 True
bool("Hello")
bool(123456)
bool(["apple", "cherry", "banana"])

# 以下实例都将返回 False
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

"""
常见运算符
加法（+）：a + b
减法（-）：a - b
乘法（*）：a * b
除法（/）：a / b
求余（%）：a % b
求商（//）： a // b
求幂（**）：a ** b
"""

# python中除法得到的类型是float
print(type(2 / 2))
print(2 / 2 == 1.0)
print(1 == 1.0)
print(1 == 2 / 2)

# 复数
print('Complex number: ', 1 + 1j)
print('Multiplying complex numbers: ', (1 + 1j) * (1 - 1j))

print("not 1:", not 1)
print("1", 1)

"""
is：如果两个变量是同一个对象，则返回 true（x 是 y）
is not：如果两个变量不是同一个对象（x 不是 y），则返回 true
in：如果查询的列表包含某个项（x in y），则返回 True
not in：如果查询的列表没有某个项（x in y），则返回 True
"""
print("'w' in 'wen':", 'w' in 'wen')
print("'we' is 'we':", 'we' is 'we')

#按位运算符 & |
print("1 & 1:",1 & 1)

#逻辑运算符 and or not

print("------exercise------")
age = 26
height = 1.78
comp = 1+1j
print("请分别输入三角形的底和高")
bottom = float(input("底："))
height = float(input("高："))
print("三角形的面积是：",bottom*height/2)


print("points between (2,2) and (6,10) has the k:", (10-2)/(6-2)
      ,"and euler distance is:", ((10-2)**2+(6-2)**2)**0.5)

print("'on' in 'python' and 'on' in 'dragon':",'on' in 'python' and 'on' in "dragon")

v = int(input("请输入一个自然数:"))
print(v,"是一个偶数" if (v%2 == 0) else "不是一个偶数")


print(int(7/2) == int(2.7))

print("int(9.8):", int(9.8))

year = int(input("请输入年："))
print(year,"年一共",year*356*24*60*60,"秒")
table = [[1,1,1,1,1],[2,1,2,4,8],[3,1,3,9,27],[4,1,4,16,64],[5,1,5,25,125]]
print(table)

for i in [1,2,3,4,5]:
    print(i,1,i,i*i,i*i*i)


