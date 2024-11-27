import requests # 导入模块

url = 'https://www.w3.org/TR/WD-html40-970708/html40.txt' # 定义要读取的地址变量

response = requests.get(url) # 请求地址并获取返回数据
print(response)
print(response.status_code) # 打印状态, success:200
print(response.headers)     # 头信息
print(response.text) # 查看所返回的数据文本 注意如果地址无法访问时候内容是404


# import requests
# url = 'https://v0.yiketianqi.com/api?unescape=1&version=v91&appid=43656176&appsecret=I42og6Lm&ext=&cityid=&city='  # 国内可访问天气接口
# response = requests.get(url)
# print(response)
# print(response.status_code)
# weather = response.json()
# print(weather)

"""
关于更多包的信息
数据库

SQLAlchemy or SQLObject - 对几个不同数据库系统的面向对象访问
pip install SQLAlchemy
Web开发

Django - 高级web框架
pip install django
Flask - 基于Werkzeug的Python微框架
pip install flask
HTML爬虫

Beautiful Soup - 是一个HTML/XML的解析器，主要的功能也是如何解析和提取HTML/XML数据。
pip install beautifulsoup4
PyQuery - 在Python中实现jQuery;显然比BeautifulSoup快。
XML 语言

ElementTree - Element类型是一种简单但灵活的容器对象，用于在内存中存储层次数据结构，例如简化的XML信息集。注意:Python 2.5及以上版本在标准库中带有ElementTree
GUI桌面程序

PyQt - 跨平台的桌面程序框架
TkInter - 传统的Python用户界面工具包（内置）
数据分析，数据科学和机器学习

Numpy: Numpy(numeric python) 被称为 python 中最受欢迎的机器学习库之一
Pandas: 作为数据分析、数据科学和机器学习库，提供高级数据结构和各种各样的分析工具。
SciPy: 是一个面向应用程序开发人员和工程师的机器学习库。SciPy库包含优化、线性代数、集成、图像处理和统计模块。
Scikit-Learn: 针对Python 编程语言的免费软件机器学习库。通常被认为是处理复杂数据的最佳库之一
TensorFlow: 谷歌建立了一个机器学习库
Keras: 是一个 Python深度学习框架。
Network:

requests: 一个可以发送请求到服务器(GET, POST, DELETE, PUT)的包
pip install requests
"""