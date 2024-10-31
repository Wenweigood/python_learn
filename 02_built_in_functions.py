# 内置函数使用
import math

print(len([1, 2, "123"]))
# help(str)
print(min(1, 2, 3))

# 进行比较时必须是能相互比较的数，否则报TypeError，例如str和int。'1'也算str
print(min(1, 2, 0.1))

# 变量名，python中一般采用蛇形（snake_case）变量命名约定
a = 1
_a = 2
文名称 = 2.3  # not recommend
print(min(a, _a, 文名称))
print('Hello', 'World!', sep=",")
name = 'ww123'
print(name, len(name))

# 多变量声明用逗号分隔，并且值一一对应
name, country, age = 'MegaQi', 'China', 18

# 获取用户输入
nick_name = input('请输入你的昵称: ')
# 打印变量值
print(nick_name)

print([1, 2, [123]])
print(type([1, 2, [123]]))
print(type(zip([1, 2], [3, 4])))  # zip（二维矩阵）

# int 转 float
num_int = 10
print('num_int', num_int)  # 10
num_float = float(num_int)
print('num_float:', num_float)  # 10.0

# float 转 int
gravity = 9.81
print(int(gravity))  # 9 取整

# int 转 str
num_int = 10
print(num_int)  # 10
num_str = str(num_int)
print(num_str)  # '10'

# str 转 int 或 float
num_str = '10.6'
# print('num_int', int(num_str))      # 这里会报错，浮点字符在python3.5+ 中不能直接用int转
print('num_float', float(num_str))  # 10.6

# str 转 list
name = 'MegaQi'
print(name)  # 'MegaQi'
name_to_list = list(name)
print(name_to_list)  # ['M', 'e', 'g', 'a', 'Q', 'i']

name = {"k1": 1, "k2": 2}
name_to_list = list(name.values())  # 必须是可迭代类型的(iterable)
print(name_to_list)  # ['M', 'e', 'g', 'a', 'Q', 'i']

name, age, country = 'w', 20, 'china'
print("name:", name, " age:", age, " country:", country)

num_1, num_2 = 5, 4
total = num_1+num_2
diff = num_1- num_2
product = num_1*num_2
division = num_1/num_2
reminder = num_1%num_2
exp = num_1**num_2
entropy = num_1//num_2
print(total,diff,product,division,reminder,exp,entropy)

radius = 30
area_of_circle = radius * radius * math.pi
print("pi:", math.pi, " area of circle:", area_of_circle)
radius = float(input("圆的半径是："))
print("area of circle:", radius * radius * math.pi)
name, age, country = input("名字"),input("年龄"),input("国家")
print(name,age,country,sep=";")



