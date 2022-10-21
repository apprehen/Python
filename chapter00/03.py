# 计算1~100的和及平均数
# sum = 0
'''for i in range(1,101):
    sum += i;
aver = sum/100
print(sum,aver)'''
'''import random
arr = [None] * 10
for i in range(0,10):
    arr[i] = random.randint(1,100)
    print(arr[i])
print(max(arr),arr.index(max(arr)))'''
Num = int(input("输入一个值:"))
a = int(Num%10)
b = int(Num/10)%10
c = int(Num/100)%10
d = int(Num/1000)
print(a+b+c+d)

