# ## Python 爬虫比较常用的库是 request 而不在使用传统的 socket 套接字去建立通道连接
# # socket 方式访问页面
# import socket
# sock_client = socket.socket(family=socket.AF_INET,type=socket.SOCK_STREAM)
# # 建立信道连接 80为默认端口
# sock_client.connect(("www.people.com.cn",80))
# pathname = '/n1/2022/1013/c1001-32544874.html' # 具体的页面
# hostname = 'www.people.com.cn'
# req_line = "GET {0} HTTP/1.0\r\nHost: {1}\r\n\r\n".format(pathname, hostname)
# print(req_line)
# sock_client.send(req_line.encode(encoding="utf-8"))
# raw_reply = b''
# while True:
#     more = sock_client.recv(8192)
#     if not more:
#         break
#     raw_reply += more
# sock_client.close()
# print(raw_reply.decode())
# # 首先安装 pip install requests
import html
import requests
# url = 'https://www.pixiv.net/'
# 伪装成浏览器
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
# }
# web_data = requests.get(url,headers=headers)
# print(web_data)
# print(type(web_data))
# print(web_data.headers)
# print(web_data.request.headers)
# print(web_data.text == web_data.content.decode('utf-8'))
# print(web_data.text)
# http://httpbin.org/headers  测试网站
# url = "http://httpbin.org/headers"
# r = requests.get(url)
# print(type(r))
# print(r.text)
# ## decode 解码
# # print(r.content.decode())
# # 客户端请求的头部
# # print(r.request.headers)
# # 服务端响应的头部
# # print(r.headers)
# ###########################
# # 封桢
# r = requests.get("https://www.hdu.edu.cn/news/important_26525")
# print(r.text)
# print(r.content)
# print(r.content.decode('utf-8'))
# print(r.content.decode('utf-8') == r.text)
# print(r.status_code)
# r = requests.get("http://httpbin.org/ip")
# # print(r.text)
# ## 转化为json格式 类似于字典
# print(r.json())
# print(r)
# ##########################
# # HTTP方法
# r = requests.get("http://httpbin.org/get",params={
#     'name': '张三',
#     'password': '123'
# })
# print(r.request.headers)
# print(r.headers)
# print(r.text)
# ## post 方法一般用于表单的提交 不会显示在网页上
# r = requests.post("http://httpbin.org/post",
#                   data={
#                       'name':'test',
#                       'password':'123'
#                   })
# print(r.text)
# print(r.request.body)
# ###################################
# # Session
# # 创建一个session对象
# s = requests.Session()
## 用Session对象发出请求，设置cookies
# r = s.get('http://httpbin.org/cookies/set/test/123456') #类似与request请求，多了可以提交的信息
# print(r.headers)
# print(s.headers)
# print(r.history)
# print(r.request.headers)
# print(r.history[0].headers)
# print(r.history[0].text)
# # print(r.content.decode('utf-8'))
# # print(r.content.decode('utf-8')==r.text)
# # 用session对象发出另外一个get请求，获取cookies
# r = s.get("http://httpbin.org/cookies")
# # # print(r.text)
# print(r.request.headers)
# print(r.cookies.items())
# # # 更新客户端请求头中的选项配置
# s.headers.update({
#     'Accept-language': 'en-Us,en;q=0.8',
#     'test': '123',
# })
# r = s.get("http://httpbin.org/headers")
# print(r.text)
# #####################################################
# # 内容类型
# # r = requests.get('http://httpbin.org/encoding/utf-8')
# # r = requests.get('http://httpbin.org/encoding/gbk')
# # print(r.headers)
# # print(r.text)
# ######################################################
# # HTTP 认证
# r = requests.get('http://httpbin.org/basic-auth/test/123456')
# print(r.status_code,r.headers)
import base64
# print(base64.b64decode('dGVzdDoxMjM0NTY=').decode())
# sess = requests.Session()
# auth = base64.b64encode(b'test:123456').decode('ascii')
# print(sess.headers)
# print(auth)
# sess.headers.update({'Authorization':'Basic' + auth})
# print(sess.headers)
# r = sess.get('http://httpbin.org/basic-auth/test/123456')
# # print(r)
# # print(r.request.headers)
# # print(r.request.headers == sess.headers) #true 都表示用用户的请求头
# # print(r.headers)
# # print(r.text)
# ############################
# # json解析
# import json
# # mystr = '{\n  "authenticated": true, \n  "user": "test"\n}\n'
# # res = json.loads(mystr)
# # print(res)
# ###########################
# # xpath语法
from lxml import etree
r = requests.get("http://www.hdu.edu.cn/news/important_26525")
# print(r.text)
hpage = etree.HTML(r.text)
# print(type(hpage))
ele_list = hpage.xpath('//li')
# print(ele_list)
# print(etree.tostring(ele_list[10],encoding='utf-8'))
# print(html.unescape(etree.tostring(ele_list[10]).decode('utf-8')))
ele_list = hpage.xpath('//li[@data-id]')
# print(ele_list)
# print(html.unescape(etree.tostring(ele_list[0]).decode('utf8')))
# print(ele_list[0].xpath("div[2]/text()"))
# print(ele_list[0].xpath("div[@class='con']/text()"))
# print(ele_list[0][1].text)
myarr = [child.tag for child in ele_list[0]]
# print(myarr)
myarrtext = [child.text for child in ele_list[0]]
# print(myarrtext)
# for ele in ele_list:
#     print(ele[2].text,'---->',ele[1].text)
content  = hpage.xpath("/html/body/div[1]/div[2]/div[3]/div[2]/div[1]")
# print(content[0].text)
content = hpage.xpath("//div[@class='article']")
# print(content)
content = content[0].xpath("div[@class='con']")
# print(etree.tostring(content[0]))
# print(html.unescape(etree.tostring(content[0]).decode('utf-8')))
from IPython.display import HTML
htmltext = html.unescape(etree.tostring(content[0]).decode('utf8'))
htmltext = htmltext.replace('/uploads', 'http://www.hdu.edu.cn/uploads')
print(HTML(htmltext).data)

