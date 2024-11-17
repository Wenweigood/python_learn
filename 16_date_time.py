from datetime import datetime

print(dir(datetime))

now = datetime.now()
print(now)
print('day',now.day)
print('month',now.month)
print('year',now.year)
# seconds from 1970/1/1 float type
print('timestamp',now.timestamp())
print(f'{now.day}/{now.month}/{now.year}')

# 时分秒大写，年大写，月、日小写
t = now.strftime("%H:%M:%S")
print("time:", t)

from datetime import date
d = date(2022, 5, 1)
print(d)                             # 指定时间 2022-05-01
print('Current date:', d.today())    # 当前时间 2023-01-07

# 将今天的时间给予today对象
today = date.today()
print("Current year:", today.year)   # 2023
print("Current month:", today.month) # 1
print("Current day:", today.day)     # 7

diff = date(2024,11,15) - date(2024,11,17)
print('diff',diff)
diff = datetime(2024,11,17,11,11,11) - datetime(2024,11,17,11,10,10)
print(f'diff:{diff},diff_type:{type(diff)},diff_seconds:{diff.total_seconds()}')

print('------exercise------')

print(now.strftime("%m/%d/%Y, %H:%M:%S"))
date_str = '2023年1月1日'
print(datetime.strptime(date_str,'%Y年%m月%d日'))

print('seconds from 1970/1/1', now.timestamp())