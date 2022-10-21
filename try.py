# 目标网站 'https://www.pixiv.net/'
# 引入request 请求库
import requests
from pyquery import PyQuery as pq
from fake_useragent import UserAgent
import os
# import datetime
# from urllib.parse import urljoin
# from concurrent.futures import ThreadPoolExecutor

# 随机请求头
ua = UserAgent(verify_ssl=False, path='./fake_useragent0.1.11.json')
# 网站url
base_url = 'https://www.pixiv.net/artworks/101999071'
path = 'D:/P站测试一下'
def ua_random():
    headers = {
        'use_agent': ua.random
    }
    return headers
# 下载函数
def download():
    def download(path, name, image):
        save_path = path + name + '.jpg'
        with open(save_path, 'wb') as f:
            f.write(image)

if not os.path.exists(path):
    os.mkdir(path)
response = requests.get(url=base_url,headers=ua_random())
if response.status_code == 200:
    response.encoding = 'utf-8'
    html = response.text
    doc = pq(html)
    print(doc)
    links = doc('a img')
    # print(links)
    i = 1
    # for link in links.items():
    #     src = link.attr('src')
    #     image = requests.get(url=src, headers=ua_random()).content
    #     image_name = name = f'_{i}'
    #     download(path, image_name, image)





















# # 获取当前日期
# today = datetime.date.today()
# # 创建爬取网站的文件夹
# path_1 = 'D:/P站每日榜单'
# if not os.path.exists(path_1):
#     os.mkdir(path_1)
#
# # 如果有重名
# path_2 = f'D:/P站每日榜单/{today}/'
# if not os.path.exists(path_2):
#     os.mkdir(path_2)
#
# # 随机请求头防止被封
# def ua_random():
#     headers = {
#         'use_agent': ua.random
#     }
#     return headers
#
# #放回具体
#
# # 爬取具体的页面内容
# def scrapCon(url):
#     try:
#         response = requests.get(url=url,headers=ua_random())
#         if response.status_code == 200:
#             response.encoding = 'utf-8'
#             return response.text
#     except requests.RequestException:
#         print(f'{url}网站爬取失败捏')
#
# #对具体页面就行解析
# def scrapExp(html):
#     doc = pq(html)
#     # 利用PyQuery库对网页进行分析
#     links = doc()