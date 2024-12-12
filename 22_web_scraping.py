# python爬虫
import requests
from bs4 import BeautifulSoup

# url = 'https://www.baidu.com'
#
# # 让我们使用网络请求url，获取返回的数据
# response = requests.get(url)
# # 检查返回状态，200表示正常
# status = response.status_code
# print(status)
#
# content = response.content
# soup = BeautifulSoup(content, 'html.parser')

# print(soup.title)
# print("<",soup.title.get_text(),">")

print('------exercise------')

url = 'https://movie.douban.com/chart'
headers = {
    'authority': 'movie.douban.com',
    'method': 'GET',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-encoding': 'gzip, deflate, br, zstd',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'referer': 'https://movie.douban.com/',
    'sec-ch-ua': '"Microsoft Edge";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    'sec-ch-ua-platform': '"Windows"',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0'
}
response = requests.get(url, headers=headers)
content = response.content
if content is not None:
    soup = BeautifulSoup(content, 'html.parser')
    # 根据源码找content字段
    content = soup.find(id = 'content')
    # 根据源码找a标签
    for a in content.find_all('a'):
        # 每个标题有两个a标签，只要其中一个有title字段的
        if('title' in a.attrs):
            print(a['title'])
    # for h2 in movies.find_all('h2'):
    #     print(h2.contents[0])
