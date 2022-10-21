## 爬取网站 'https://www.vilipix.com' 的每日榜单图片
# 实现可以进行功能选择 1.每天，2.每周，3每月
import requests
from pyquery import PyQuery as pq
from fake_useragent import UserAgent
import os
import datetime
from urllib.parse import urljoin
from concurrent.futures import ThreadPoolExecutor

#调用随机请求头
ua = UserAgent(verify_ssl=False, path='./fake_useragent0.1.11.json')
# 网站的基底url
base_url = 'https://www.vilipix.com'
# 获取当前日期 (当前的url是根据日期作为哈希值进行的寻址)
today = datetime.date.today()
