import requests
from pyquery import PyQuery as pq
from fake_useragent import UserAgent
import os
import datetime
from urllib.parse import urljoin
from concurrent.futures import ThreadPoolExecutor
import fake_useragent
from fake_useragent import UserAgent, VERSION
# location = './fake_useragent%s.json' % fake_useragent.VERSION
## 随机请求头
ua = UserAgent(verify_ssl=False,path='./fake_useragent0.1.11.json')
## 网站url
base_url = 'https://www.vilipix.com'
## 获取当前日期
today = datetime.date.today()
# 获取昨天的日期，并用于构建url
today_str = (datetime.date.today() + datetime.timedelta(days=-1)).strftime('%Y%m%d')
# 分布创建属于当日榜单的文件夹
path_1 = 'D:/vilipix每日榜单'
if not os.path.exists(path_1):
    os.mkdir(path_1)

path_2 = f'D:/vilipix每日榜单/{today}/'
if not os.path.exists(path_2):
    os.mkdir(path_2)

def ua_random():
    headers = {
        'use_agent': ua.random
    }
    return headers

def scrap_page(url):
    try:
        response = requests.get(url=url, headers=ua_random())
        if response.status_code == 200:
            response.encoding = 'utf-8'
            return response.text
    except requests.RequestException:
        print(f'{url} 不可爬取！！')

def scrap_index(page):
    url =f'{base_url}/ranking?date={today_str}&mode=daily&p={page}'
    return url

# 对页面进行解析
def parse_index(html):
    doc = pq(html)
    links = doc('#_layout .illust-content li .illust a')
    for link in links.items():
        href = link.attr('href')
        name = href.split('/')[-1]
        detail_url = urljoin(base_url,href)
        page_count = link('.page-count span').text()
        yield detail_url,page_count,name

# 下载图片
def download(path,name,image):
    save_path = path + name + '.jpg'
    with open(save_path,'wb') as f:
        f.write(image)

# 详情页内只有一张图片时
def detail_index_1(html,name,path):
    doc = pq(html)
    link = doc('.illust-pages li a img').attr('src')
    image = requests.get(url=link,headers=ua_random()).content
    download(path,name,image)

# 详情页内有超过一张图片时调用
def detail_index_more(html,name,path):
    doc = pq(html)
    links = doc('.illust-pages li a img')
    i = 1
    for link in links.items():
        src = link.attr('src')
        image_name = name + f'_{i}'
        image = requests.get(url = src,headers=ua_random()).content
        download(path,image_name,image)

def main(page):
    html = scrap_index(page)
    details = parse_index(html)
    for detail in details:
        detail_url = detail[0] # 详情页的url
        num = details[1] # 详情页的图片数量
        name = details[2] # 给详情页命名
        detail_html = scrap_page(detail_url)
        if num==1:
            detail_index_1(detail_html,name,path_2)
        else:
            path_3 = f'D:/vilipix每日榜单/{today}/{name}/'
            if not os.path.exists(path_3):
                os.mkdir(path_3)
            detail_index_more(detail_html, name, path_3)
        print('*'*10,f'{name}下载完毕','*'*10)


if __name__ == '__main__':
    pages = list(range(1, 11))
    with ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(main, pages)