#多行字符串使用""" 或者 '''创建
str = """
123
wen
vi
"""
print(str)

#多行字符串在拼接中视作单行字符串，在各分行处有换行符\n
a = "a"
b = "b"
c = """
123
345
"""
e = "e"
f = """fff
ff
f"""
d = a + b + c + e + f
print(d)

"""
格式化字符串——————与java一致
%s - 字符
%d - 整数
%f - 浮点数
"%.数字f" - 浮点数固定小数点后几位
"""
formated_str = "my name is %s, i am %d years old"%("wen",20)
print(formated_str)

radius = 10
pi = 3.14
area = pi * radius ** 2
# 表示浮点后边保留两位小数
formated_string = 'The area of circle with a radius %d is %.2f.' %(radius, area)
print(formated_string)

"""
三种格式化字符串生成方式
str%(args)
str.format(args)
f'expressions'
"""
print('%s,%d,%.2f'%('s',1,2.345))
print('%s,%d,%.2f'.format('s',1,2.345))
print(f'{123}+{123}={123+123}')#运行时计算/注入中括号内的表达式/值，速度最快
print(f'{formated_string},.;:?/{formated_str}')

#解包字符(变量数目必须能够对应，否则解包失败)
language = 'Python'
a,b,c,d,e,f = language # 将序列字符拆分到变量中
print(a) # P
print(b) # y
print(c) # t
print(d) # h
print(e) # o
print(f) # n

#下标访问 from 0 to len-1
print("123"[1],"is",2)

#字符串切片 str[beginIndex:endIndex:step]
#beginIndex:inclusive、endIndex:exclusive、step:步长
str = 'abcdef'
print(str[0:3],str[0:5:2])
print(str[:3],str[3:])
print(str[:])
print(str[-1:])#-1表示最后一个元素的位置

greeting = 'Hello, World!'
print(greeting[::-1])
print(greeting[-1::-1])#step = -1 负数索引表示倒着取，从最后一个元素开始计数
# !dlroW ,olleH

"""
capitalize()：将字符串的第一个字符转换为大写字母
Count()：返回字符串中给定字符出现次数。语法 count(substring, start=.., end=..)。其中start为开始索引，end为结束索引。
startswith(): 检查某字符串是否已某个特殊字符串值开始
endswith()：检查字符串是否以指定的结尾结束。
expandtabs()：方法把字符串中的 tab 符号 \t 转为空格，tab 符号 \t 默认的空格数是 8。在第 0、8、16...等处给出制表符位置，如果当前位置到开始位置或上一个制表符位置的字符数不足 8 的倍数则以空格代替。
find()：返回子字符串第一次出现的索引，如果没有找到则返回-1。
rfind()：返回子字符串最后一次出现的索引，如果没有找到则返回-1。
format()：将字符串格格式化输出。
index()：返回给定值第一个匹配项的索引位置，函数形式index(x[, start[, end]]) ，其中附加参数可指定开始（默认0）和结束（默认-1）位置。如果子字符串没有匹配则抛出了ValueError异常。
    区别说明：find()函数和index()函数功能类似。区别在于找不到的返回值不同，前者返回-1，后者异常ValueError: substring not found
isalnum(): 检查字符串是否仅为字符数字组合
isalpha(): 检查是否所有字符串元素都是字母字符(a-z和a-z)
isdecimal(): 检查字符串中的所有字符是否都是十进制(0-9)
isdigit(): 检查字符串中的所有字符是否都是数字(0-9和一些用于数字的其他unicode字符)
isnumeric(): 检查字符串中的所有字符是否都是数字或与数字相关的（很像isdigit()，但接受更多的符号，比如½)
isidentifier(): 检查一个有效的标识符，即检查一个字符串是否是一个有效的变量名
islower(): 检查字符串中的所有字母字符是否都是小写
isupper(): 检查字符串中的所有字母字符是否都是大写
join(): 返回一个连接后的字符串。和+一样
strip(): 剔除开头和结尾符合指定字符，并返回新的字符串
replace(): 字符串替换
split(): 字符串拆分, 使用给定的字符串或空格（不指定时候默认）字符
title(): 字符串中所有单词首字母大写
swapcase(): 将字符串中所有大写字符转小写，反之小写转大写
"""
print('------exercise------')
print("wen".replace('n','i'))
print("Coding For All"[-1])
print("coding for all".title().endswith('All'))
print("".join(["1","2","3"]))

print('Name\tAge\tCountry\tCity')
print('Asabeneh\t250\tFinland\tHelsinki')

# 添加制表符或四个空格
print('Days\tTopics\tExercises')
print('Day 1\t5\t5')
print('Day 2\t6\t20')
print('Day 3\t5\t23')
print('Day 4\t1\t35')