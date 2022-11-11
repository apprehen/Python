from io import BytesIO
from typing import final
import requests
import re
import os
from PIL import Image
import time
from fake_useragent import UserAgent
import random
import urllib3
import datetime
import fake_useragent
# 设置随机请求头
ua = UserAgent(verify_ssl=False, path='./fake_useragent0.1.11.json')
print(fake_useragent.VERSION)
# 请求随机头
def ua_random():
  headers = {
      'use_agent': ua.random
  }
  return headers

# 模式选择入口
def __init():
  # 今日 本周 本月 新人 原创 受男性欢迎 受女性欢迎
  mode = ''
  mark = int(input("请选择你需要下载的类型\n0---今日\n1---本周\n2---本月\n3---新人\n4---原创\n5---受男性欢迎\n6---受女性欢迎\n"))
  if mark==0:
    mode = 'daily'
  elif mark==1:
    mode = 'weekly'
  elif mark==2:
    mode = 'monthly'
  elif mark==3:
    mode = 'rookie'
  elif mark==4:
    mode = 'original'
  elif mark==5:
    mode = 'male'
  elif mark==6:
    mode = 'female'
  else:
    print("输入的选项不对，即将退出程序")
    os._exit(0)
  return mode

# 创建下载文件路径
def creatpath(mode,today):
  path = f'D:/pixiv_image_{mode}/'
  path_2 = f'D:/pixiv_image_{mode}_{today}'
  if not os.path.exists(path):
    os.mkdir(path)
    return path
  if not os.path.exists(path_2):
    os.mkdir(path_2)
    return path_2

# 封装成函数 接受mode参数
def scape(mode,today):
  father = "https://www.pixiv.net/"
  url = f'https://www.pixiv.net/ranking.php?mode={mode}'
  child_url_list = []
  resp = requests.get(url,headers=ua_random())
  # 找到img属性的 href 并爬取 
  obj=re.compile(r"<div class=\"ranking-image-item\"><a href=\"(?P<image_URL>.*?)\"class",re.S)
  results = obj.finditer(resp.text)
  resp.close()
  # 将获取的href 放入数组中
  for result in results:
    list = result.group('image_URL')
    child_url=father+list.strip("/")
    child_url_list.append(child_url)
  # 获取原图片
  obj1 = re.compile(r"\"original\":\"(?P<download_URL>.*?)\"")
  # 注意 headers 应该从之前的网页进去
  headers = {'Referer':'https://www.pixiv.net/'}
  root = creatpath(mode,today)
  flag = 0
  for herf in child_url_list:
    if (flag>52):
      break
    final = requests.get(herf,headers=ua_random())
    real_image_url = obj1.search(final.text)
    final.close()
    DL_URL=real_image_url.group()
    path_img = root + str(DL_URL).split('/')[-1]
    pic = requests.get(DL_URL.split('"')[-2], headers=headers, verify=False, timeout=5)
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    # 储存在文件夹中
    image = Image.open(BytesIO(pic.content))
    image.save(f"{path_img.split('.')[-2]}.png", "png")
    print("SUCCESS!")
    flag = flag + 1
    time.sleep(3)

# 主程序入口
if __name__ == '__main__':
  # 获取当前时间
  today = datetime.date.today()
  # 获取模式的选择
  mode = __init()
  # 进入程序
  scape(mode,today)

