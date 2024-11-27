# 正则表达式
import re

"""
re.match: 只在字符串的第一行开始搜索，如果找到则返回匹配的对象，否则返回None。
re.search: 如果字符串(包括多行字符串)中有匹配对象，则返回匹配对象。
re.findall: 返回包含所有匹配项的列表，如果没有匹配则返回空列表。
re.split: 方法按照能够匹配的子串将字符串分割后返回列表。
re.sub: 查找并替换一个或者多个匹配项。
"""

txt = 'I love to teach python and javaScript'
# 本身反馈一个 span 对象
match = re.match('I love to teach', txt, re.I)  # re.I 不区分大小写
print(match)  # <re.Match object; span=(0, 15), match='I love to teach'>

# 进一步我们可以使用span()获取匹配的起始位置和结束位置的元组值
span = match.span()
print(span)  # (0, 15)

# 再进一步可以打印出拆分的起始和结束索引，以及使用分片获取匹配字符串
start, end = span
print(start, end)  # 0, 15
substring = txt[start:end]
print(substring)  # I love to teach

import re

txt = 'I love to teach python and javaScript'
match1 = re.match('I like to teach', txt, re.I)
print(match1)  # None

# match要求必须从开头开始匹配
match2 = re.match('love', txt)
print(match2)  # None
print(re.match('I * love', txt))

# search则是针对整个字符串进行匹配
print(re.search('love', txt))

# 返回所有匹配
print(re.findall('t', txt))

import re

txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

matches = re.findall('Python|python', txt)
print(matches)  # ['Python', 'python']

#
matches = re.findall('[Pp]ython', txt)
print(matches)  # ['Python', 'python']

import re

txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

match_replaced = re.sub('Python|python', 'JavaScript', txt, re.I)
print(match_replaced)  # JavaScript is the most beautiful language that a human being has ever created.

# 或者
match_replaced = re.sub('[Pp]ython', 'JavaScript', txt, re.I)
print(match_replaced)  # JavaScript is the most beautiful language that a human being has ever created.

import re

txt = '''%I a%m te%%a%%che%r% a%n%d %% I l%o%ve te%ach%ing. 
T%he%re i%s n%o%th%ing as r%ewarding a%s e%duc%at%i%ng a%n%d e%m%p%ow%er%ing p%e%o%ple.
I fo%und te%a%ching m%ore i%n%t%er%%es%ting t%h%an any other %jobs. 
D%o%es thi%s m%ot%iv%a%te %y%o%u to b%e a t%e%a%cher?'''

replaced = re.sub('%', '', txt)
print('replaced:', replaced)

print(re.split('%', txt))

"""
在以往我们声明一个变量，使用的是单引号或者双引号。如果要声明一个正则变量则是 r''
"""

regex = r'apple'
txt = 'Apple and banana are fruits. An old cliche says an apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away. '
print(re.findall(regex, txt), re.I)
print('type of regex:', type(regex))  # type of regex: <class 'str'>

"""
re.I：匹配对大小写不敏感
re.M：多行匹配（影响 ^ 和 $）
re.S：使 . 匹配包括换行在内的所有字符

[]: 一组字符
[a-c] 表示 a 或 b 或 c
[a-z] 表示 小写 a 到 z 任意字符
[A-Z] 表示 大写 A to Z 任意字符
[0-3] 表示 0 或 1 或 2 或 3
[0-9] 表示0 到 9 任意数字
[A-Za-z0-9] 表示任意单字符, 即 小写字母a到z, 大写字母A到Z 或数字0到9

\: 转义特殊字符
\d 表示 匹配任意数字，相当于 [0-9].
\D 表示 匹配任意非数字
\w 任何单字字符
. : 匹配任意字符（除了换行符 \n）
^: 匹配开头
r'^substring' 例如 r'^love', 必须以love开头的句子
r'[^] 表示不在[]中的字符，例如 r'[^abc] 表示不是a, 不是b, 不是c。即除a,b,c之外的字符
$: 匹配结尾
*: 0或多个次
r'[a]*' 表示可以不出现，或者可以出现多次
+: 0或多个次
r'[a]+' 表示至少一次或多次
?: 0或1次
r'[a]?' 表示零次或一次
{n}：精确匹配个数
{3}: 表示 正好3个字符
{3,}: 表示 至少3个字符
{3,8}: 表示 3到8个字符
|: 不是就是（或）
r'apple|banana' 表示要么是 apple 要么是 banana
(): 正则表达式分组并记住匹配的文本
"""

# 匹配小写和大写
import re

regex_pattern = r'[Aa]pple'
txt = 'Apple and banana are fruits. An old cliche says an apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away.'
matches = re.findall(regex_pattern, txt)
print(matches)  # ['Apple', 'apple']

import re

regex_pattern = r'[a].'  # 小写a和任意
txt = '''Apple and banana are fruits'''
matches = re.findall(regex_pattern, txt)  # 匹配多个项目
print(matches)  # ['an', 'an', 'an', 'a ', 'ar'] 分别对应and中an，banana中an、an、a空格，are中ar

regex_pattern = r'[a].+'  # . 任意字符, + 一次或多次（连续）
matches = re.findall(regex_pattern, txt)
print(matches)  # ['and banana are fruits']
print(re.findall('[a].{2}', txt))

print('------exercise------')
paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'
regex = r'[^. ]+'
lst = re.findall(regex, paragraph)
print(lst)
word_dict= dict()
for word in lst:
    if word in word_dict:
        word_dict[word]+=1
    else:
        word_dict[word]=1
word_tuple = [(a,b) for b,a in word_dict.items()]
print(sorted(word_tuple, reverse=True))