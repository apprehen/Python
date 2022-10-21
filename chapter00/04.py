import math
# 判断是否为质数
def IsPrime(x):
    for i in range(2, int(math.sqrt(x) + 1)):
        if (x % i) == 0:
            return False
    return True
#测试1~100的所有整数，根据IsPrime函数的返回结果，将返回True的添加入列表变量listPrimeA
'''listPrimeA =[2]
for i in range(3,101):
    if IsPrime(i):
        listPrimeA.append(i)
print(listPrimeA)'''
#将1~100的所有整数添加如列表变量listPrimeB
#对listPrimeB中的元素进行IsPrime函数测试，删除返回False的元素
listPrimeB = list(range(2,101))
listPrimeB = filter(lambda x:IsPrime(x) == True,listPrimeB)
newlist = []
for i in listPrimeB:
    newlist.append(i)
print(newlist)
