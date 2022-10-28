from cgitb import reset
import requests
import os
import base64
from PIL import Image
from io import BytesIO
import random
import time
def sele():
  mark = int(input("请选择你要下载的类型:\n1 --- 随机壁纸(全部图)\n2 --- 随机壁纸(无色图)\n3 --- 壁纸推荐\n4 --- 银发\n5 --- 兽耳\n6 --- 星空\n7 --- 竖屏壁纸\n8 --- 横屏壁纸\n9 --- 随机色图(还在开发捏)\n"))
  if mark==1:
    mode = 'random'
  elif mark==2:
    mode = 'iw233'
  elif mark==3:
    mode = 'top'
  elif mark==4:
    mode = 'yin'
  elif mark==5:
    mode = 'cat'
  elif mark==6:
    mode = 'xing'
  elif mark==7:
    mode = 'mp'
  elif mark==8:
    mode = 'pc'
  elif mark==9:
    print("说了还在开发中，别那么心急嘛！！")
    os._exit(0)
  else:
    print("输入的选项不对，即将退出程序")
    os._exit(0)
  return mode

def get_url(urls,mode):
  '''
    具体形式 url?sort=mode
    url 为 urls 中的任意一种
    mode 为传入的模式捏
  '''
  return f'{urls[random.randint(0,3)]}?sort={mode}'

def spider(url,img_name,mode):
  i = 1
  # 保存图片
  path_name =  time.strftime('%Y_%m_%d_%H', time.localtime())
  path = f"D:\\iw233_image_{mode}_{path_name}"
  if not os.path.exists(path):
    os.mkdir(path)
  # 写成循环形式
  while 1:
    if i > 68:
      break
    response = requests.get(url = url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36"})
    image = Image.open(BytesIO(response.content))
    image.save(f"{path}/{img_name}_{i}.jpg")
    print("SUCCESS!")
    i = i + 1

if __name__ == '__main__':
  # 主程序入口
  # 获取时间
  img_name =  time.strftime('%Y_%m_%d_%H_%M', time.localtime())
  mode = sele()
  urls = ['https://iw233.cn/api.php','http://api.iw233.cn/api.php','https://dev.iw233.cn/api.php','http://ap1.iw233.cn/api.php']
  url = get_url(urls,mode)
  spider(url,img_name,mode)
