# I/O input/output (print)
# name = input('Please enter your name:')
# print("You Name is:",name)
# print('1024 * 768 =',1024*768) # 在输出中, 等于一个空格捏

#Python的语法比较简单，采用缩进方式，写出来的代码就像下面的样子：
# a = int(input("Please enter a Number:"))
# if a >= 0:
#     print(a)
# else:
#     print(-a)
### 当语句以冒号:结尾时,缩进的语句视为代码块,类似C语言中的 { } 并且注意Python程序是大小写敏感(感觉不如JS)

##数据类型
#- 整数
# a = int(input("Please entry the first number:")) #int为转为整形类型
# b = int(input("Please entry the second number:"))
# print("The result",a,'+',b,"=",a+b)
c = '''aa '''
# print('\\\t\\')
# print(r'\\\t\\')
# print(r'''Welcome To \n
# My Blog''')
# a = 3 > 2
# b = 3 < 5
# print(a,b)
# a = 'aaa'
# b = a
# a = 'xyz'
# print(b)
# a = b'ABC'.decode('utf-8')  #bytes类型
# print('中文'.encode('utf-8'))
# age = 18
# if age >= 18:
#     print('adult')
# elif age >= 6:
#     print('teenager')
# else:
#     print('kid')
# names = ['meigumi','kurumi','toka']
# for name in names:
#   print(name)
# sum = 0
# for x in range(101):
#   sum = sum + x
# print(sum)
# sum = 0
# n = 0
# while n<=100:
#   sum = sum + n
#   n = n + 2
# print(sum)
# n = 1
# while n<=100:
#   print(n)
#   n = n + 1
# print("END")
# n = 1
# while n<=100:
#   if n>10: # n=11时，条件满足，执行break语句
#     break # break语句会结束当前循环
#   print(n)
#   n = n + 1
# print("END")
# n = 0
# while n < 10:
#     n = n + 1
#     if n % 2 == 0: # 如果n是偶数，执行continue语句
#         continue # continue语句会直接继续下一轮循环，后续的print()语句不会执行
#     print(n)
# import random
# a = [random.randint(0,100) for i in range(50)]
# print(a)
# i = len(a) - 1
# while i >= 0:
#     if a[i]%2 == 1:
#         del a[i]
#     i-=1
# print(a)
# import random
# x = [random.randint(0,100) for i in range(20)]
# print(x)
# y = x[::2]
# y.sort(reverse=True)
# x[::2] = y
# print(x)
# x = int(input("请输入一个整数："))
# y = x
# alist = []
# blist = []
# i = 2
# while 1:
#     if x % i == 0:
#         x = x / i
#         alist.append(i)
#     else:
#         i += 1
#
#     if x == 1:
#         break
#
# for i in alist:
#     j = "%s" % i
#     blist.append(j)
#
# print("%d = " % y, end="")
# print(" * ".join(blist))
# x = int(input("请输入X的值："))
# y = 0
# if x<0:
#     y = 0
# elif (x>=0 and x<5):
#     y = x
# elif (x>=5 and x<10):
#     y = 3*x-5
# elif (x>=10 and x<20):
#     y = 0.5*x - 2
# else:
#     y = 0
# print(y)
# d = {'meigumi':95,'toka':75,'kurumi':85}
# print(d['meigumi'])
# d['meigumi'] = 67
# print(d['meigumi'])
# print('yueyun' in d)
# print(d.get('yueyun',-1))
# s =set([1,1,2,3,2,3,3])
# print(s)
# def my_abs(x):
#   if x>=0:
#     return x
#   else:
#     return -x
# print(my_abs(-99))
# import math
# def move(x,y,step,angle=0):
#   nx = x + step * math.cos(angle)
#   ny = x + step * math.sin(angle)
#   return nx,ny
# x,y = move(100,100,60,math.pi/6)
# print(x,y)
# def add_end(L=[]):
#   if L is None:
#     L=[]
#   L.append('END')
#   return L
# print(add_end())
# print(add_end())
# def calc(*numbers):
#   sum = 0
#   for n in numbers:
#     sum = sum + n * n
#   return sum
# # 首先想到的是传入一个数组或者元组
# # a = calc([1,2,3])
# # a = calc(1,3)
# # b = calc((1,3,5,7))
# # b = calc()
# a = [1,2,3,4]
# b = (1,2,3,4)
# print(calc(*a),calc(*b))
# def person(name,age,**kw):
#   print('name:',name,'age:',age,'other:',kw)
# person('meigumi',18)
# a = int(input())
# sum = 0
# Myarr = []
# for i in range(1,a+1):
#   sum+=i
#   if(i<a):
#     Myarr.append(str(i))
#     Myarr.append('+')
#   else:
#     Myarr.append(str(i))
#     Myarr.append('=')
# Mystr = ''.join(Myarr)
# print("%s%d"%(Mystr,sum))
# def person(name,age,**kw):
#   print('name:',name,'age:',age,'other:',kw)
# person('meigumi', 18, city="二次元", tag="人妻")
# extra = {'city': 'yisijie', 'job': '...'}
# person('kurumi', 18, city=extra['city'], job=extra['job'])
# def person(name,age,*,city,job):
#   print(name,age,city,job)
# person('Jack', 24, city='Beijing', job='Chaoyang')
# L = ['Michael','Sarah','Tracy','Bob','Jack']
# ##取前三个元素
# r = []
# for i in range(3):
# 	r.append(L[i])
# print(L[0:3])
# L = list(range(100))
# print(L)
# print((0,1,2,3,4,5)[:3])
# d = {'a':1,'b':2,'c':3}
# for key in d:
# 	print(key)
# for value in d.values():
# 	print(value)
# for k,v in d.items():
# 	print(k,v)
# for ch in 'ABC':
# 	print(ch)
# from collections.abc import Iterable
# a=isinstance('abc',Iterable)
# print(a)
# for i,value in enumerate(['A','B','C']):
# 	print(i,value)
# import os
# print([d for d in os.listdir('.')])
# d = {'x':'A', 'y':'B', 'z':'C'}
# print([k+'='+v for k,v in d.items()])
# L = ['Hello', 'World', 'IBM', 'Apple']
# print([s.lower() for s in L])
# a = [1,2,3,4,5,6]
# a.extend([7,8,9])
# print(a)
# a_list = [3,5,7,9,7,11]
# a_list.remove(7)
# print(a_list)
# import random
# aList=[3,4,5,6,7,9,11,13,15,17]
# ## 类似于重新洗牌
# random.shuffle(aList)
# print(aList)
# aList.sort()
# aList.sort(reverse=True)
# print(aList)
# li = [[1, 7], [1, 5], [2, 4], [1, 1]]
# li.sort()
# print(li)
# def fun(li):
#     return li[1]
# li.sort(key=fun)
# print(li)
# print(len(str(1)))
# aList =[[1, 7], [1, 5], [2, 4], [1, 1]]
# aList.sort(key = lambda x:len(str(x)))
# print(aList)
# scores = {"Zhang San": 45,
#           "Li Si": 78,
#           "Wang Wu": 40,
#           "Zhou Liu": 96,
#           "Zhao Qi": 65,
#           "Sun Ba": 90,
#           "Zheng Jiu": 78,
#           "Wu Shi": 99,
#           "Dong Shiyi": 60}
# print(scores.values())
# print(scores.items())
# highest = max(scores.values())
# lowest = min(scores.values())
# # average = sum(scores.values()*1.0/len(scores))
# highestPerson = [name for name,scores in scores.items() if scores ==highest]
# print(highestPerson)
#
# g = (x * x for x in range(10))
# print(g)
# print(next(g))
# print(next(g))
# def fib(max):
#     n,a,b = 0,0,1
#     while n<max:
#         yield b
#         a,b = b,a+b
#         n = n+1 # 步长
#     return 'done'
# f = fib(6)
# print(f)
# for f in fib(6):
#     print(f)
# s = 'apple peach banana pear'
# s = 'Hello World \n My name is LiHua'
# li = s.split()
# print(li)
# li = ['Apple','peach','banner','pear','55']
# s = '?'.join(li)
# s = '123'.join('a')
# aList = ['真由理','薰','saber','Mashiro','kurumi','meigumi','kota']
# result = ' '.join(aList)
# print(result)
# from functools import reduce
# def f(x):
#     return x*x
# # r = map(f,[1,2,3,4,5,6,7,8,9])
# # blist = list(r)
# # print(blist)
# def add(x,y):
#   return x*10+y
# reduce(add,[1,3,5,7,9])
# print(reduce(add,[1,3,5,7,9]))
# def stat(param):
#     heigest = max(param)
#     lowest = min(param)
#     averge = (sum(param)*1.0)/len(param)
#     length = int(len(param))
#     if length%2==0:
#         zhongweishu = (param[length//2] + param[length//2 - 1])/2
#     else:
#         zhongweishu = param[length//2]
#     print((averge,heigest,lowest,zhongweishu))
# a = list(range(1, 100))
# a = [1,3,2,5,6]
#
# print(stat(a))

# def box(s):
#     s = s.join([' ',' ']).join(['*','*'])+'\n'
#     top = ['*'] * len(s)
#     topstr = ''.join(top)+'\n'
#     result = s.join([topstr,topstr])
#     print(result)
# print(box('Hello World'))
# s = 'Hello World'.join([' ',' ']).join(['*','*']) +'\n'
# top = ['*'] * len(s)
# topstr = ''.join(top)+'\n'
# result = s.join([topstr,topstr])
# print(result)
# def ssum(*p):
#     sum = 0;
#     for n in p:
#         sum = sum + n*n
#     return sum
# def f(n):
#     sum = 1
#     for i in range(1,n+1):
#         sum = sum*i
#     return sum
# print('f(3)=', f(3))
# print('f(5)=', f(5))
# def square(n):
#     yield (i*i for i in range(1,n+1))
# print((square(5)))
# def permutate(plist):
#     if len(plist) <= 1:
#         yield plist
#     else:
#         for perm in permutate(plist[1:]):
#             for i in range(len(plist)):
#                 yield perm[:i] + plist[0:1] + perm[i:]
# print(list(permutate([1,2,3])))
#############################
# 定义类
class Car:
    def infor(self):
         print("This is a car")
# 定义类之后可以实例化对象
car = Car()
car.infor()
import socket
sock_client = socket.socket(family=socket.AF_INET)