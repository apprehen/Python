# # 使用 selenium + chrome 去自动化测试爬取网页
# from asyncio import sleep
# from http import cookies
# from fastapi import Cookie
# import requests
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import sys
# import os
# import time
# from fake_useragent import UserAgent
# from setuptools import Command

# ua = UserAgent(verify_ssl=False, path='./fake_useragent0.1.11.json')

# def ua_random():
#     headers = {
#         'use_agent': ua.random
#     }
#     return headers
# # executable_path 执行器路径 (放入python中script里默认不用写) 
# # pixiv榜单
# def __init():
#   # 今日 本周 本月 新人 原创 受男性欢迎 受女性欢迎
#   mode = ''
#   mark = int(input("请选择你需要下载的类型\n0---今日\n1---本周\n2---本月\n3---新人\n4---原创\n5---受男性欢迎\n6---受女性欢迎\n"))
#   if mark==0:
#     mode = 'daily'
#   elif mark==1:
#     mode = 'weekly'
#   elif mark==2:
#     mode = 'monthly'
#   elif mark==3:
#     mode = 'rookie'
#   elif mark==4:
#     mode = 'original'
#   elif mark==5:
#     mode = 'male'
#   elif mark==6:
#     mode = 'female'
#   else:
#     print("输入的选项不对，即将退出程序")
#     os._exit(0)
#   return mode

# # 将cookie转化为字典推导式
# def cookie_to_dic(cookie):
#   return {item.split('=')[0]: item.split('=')[1] for item in cookie.split('; ')}


# # 手工获取cookie
# def get_cookie():
#   login_url = 'https://www.pixiv.net/'
#   res = requests.get(url=login_url,headers=ua_random())
#   cookies = cookie_to_dic(res.cookies)
#   print(cookies)
#   # print(res)
#   # _ga = res.cookies.get('_ga')
#   # _ga_75BBYNYN9J = res.cookies.get(_ga_75BBYNYN9J)
#   # PHPSESSID = res.cookies.get(PHPSESSID)
#   # p_ab_id = res.cookies.get(p_ab_id)
#   # personalization_id = res.cookies.get(personalization_id)
#   # __utmv = res.cookies.get(__utmv)
#   # device_token = res.cookies.get(device_token)
#   # cookie = {'device_token':device_token,'p_ab_id':p_ab_id,'personalization_id':personalization_id}
#   # return cookie


# # 为selenium设置cookie
# def add_cookie(self,cookie_dict):
#   '''
#     add a cookie to your current session
#     require keys "name" and "value"
#     optional keys "path" "domain","secure","expiry  "
#   '''
#   self.execute(Command.ADD_COOKIE,{"cookie:cookie_dick"})



# # 模拟登陆
# def selelogin(mode):
#   options = webdriver.ChromeOptions()
#   options.add_experimental_option('excludeSwitches', ['enable-logging'])
#   chrome = webdriver.Chrome(options=options)
#     # 添加反爬手段
#   script = 'Object.defineProperty(navigator,"webdriver",{get:() => false,});'
#   # 每个榜单最多存有50张id(1-50) selection
#   cookies = get_cookie()
#   # 为界面设置Cookie
#   chrome.get(f"https://www.pixiv.net")
#   chrome.add_cookie(cookie_dict=cookies)
#   chrome.execute_script(script)
#   login = chrome.find_element(By.CLASS_NAME,'signup-form__submit--login')
#   login.click()
#   time.sleep(3)
#   chrome.execute_script(script)
#   chrome.find_element(By.CLASS_NAME,'degQSE').send_keys('3514392356@qq.com')
#   time.sleep(3)
#   chrome.find_element(By.CLASS_NAME,'hfoSmp').send_keys('Apprehensive1')
#   time.sleep(3)
#   chrome.find_element(By.CLASS_NAME,'fguACh').click()
#   time.sleep(3)
#   chrome.execute_script(script)


# # test = chrome.find_element('id','1') 
# # print(test)

# # 主程序的入口
# if __name__ == '__main__':
#   # 选择榜单形式
#   # resultmode = __init()
#   # 模拟登陆
#   get_cookie()
#   # selelogin(1)
