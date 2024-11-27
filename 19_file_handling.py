# 在Python中处理文件数据使用的是 open 内置方法
"""
语法形式
open('filename', mode) # 模式mode(r, a, w, x, t,b)  表示 读, 写, 更新

"r" - 英文Read表示读 - 默认值。以读的模式打开一个文件，如果文件不存在它将返回一个错误。Opens a file for reading, it returns an error if the file does not exist
"a" - 英文Append表示追加 - 以追加模式打开文件，如果文件不存在则会自动创建。Opens a file for appending, creates the file if it does not exist
"w" - 英文Write表示覆盖式写 - 以写的模式打开一个文件，如果文件不存在则创建。Opens a file for writing, creates the file if it does not exist
"x" - 英文Create表示创建 - Creates the specified file, returns an error if the file exists
"t" - 英文Text表示文本 - Default value. Text mode
"b" - 英文Binary表示字节 - Binary mode (e.g. images)
"""
import os.path

if not os.path.exists('./files'):
    os.mkdir('files')
try:
    f = open('./files/reading_file_example.txt', 'a')
    print(f)  # <_io.TextIOWrapper name='./files/reading_file_example.txt' mode='r' encoding='cp936'>>
except Exception as e:
    print('open file failed:', e)
    exit(1)
f.write('123\n')
f.write('''This is an example to show how to open a file and read.
This is the second line of the text.I love python''')
f.close()

f = open('./files/reading_file_example.txt', 'r')
txt = f.read()
print('txt', txt, '\n')

f = open('./files/reading_file_example.txt', 'r')
# 读取10个字符
txt_10 = f.read(10)
print('txt_10', txt_10, '\n')

# 读取一行
# f.readline()

# 按行读取并形成一个字符列表（包含换行符）
# f.readlines()

# 按行读取并形成一个字符列表（不包含换行符）
# f.read().splitlines()

"""
当打开一个文件，使用完的时候必须关闭它。其实有一种更高级的方式处理它。我们可以使用 with ，此方式可以自己关闭文件使用。
类比于 java中的try with resource
"""
with open('./files/reading_file_example.txt') as f:
    lines = f.read().splitlines()
    print(type(lines))
    print(lines)

if os.path.exists('./files/reading_file_example.txt'):
    os.remove('./files/reading_file_example.txt')

# json转字典

import json

# JSON
person_json = '''{
    "name": "MegaQi",
    "country": "China",
    "city": "ShangHai",
    "skills": ["JavaScrip", "React", "Python"]
}'''
# 接下来 json 转 dict
person_dct = json.loads(person_json)
print(type(person_dct))
print(person_dct)
print(person_dct['name'])

# 注意这里str必须使用""而非''
person_json = '''[1,2,1,[1,"w"]]'''
# 接下来 json 转 dict
person_dct = json.loads(person_json)
print(type(person_dct))
print(person_dct)
