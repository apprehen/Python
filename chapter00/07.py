# 规则如下：
# 　　投掷3个骰子，如果3个骰子之和小于10为小，大于10为大
# 步骤分解：
#
# 请用户输入大或小（用0,1代替）
# 投掷3个骰子，使用random库中的randint函数生成骰点大小，并依次输出骰点
# 计算骰点大小，判断用户输赢，并给出结果
import math
import random

Num = input('输入大小(0或1):')
a = random.randint(1,6)
print(a)
b = random.randint(1,6)
print(b)
c = random.randint(1,6)
print(c)
ComNum = a + b + c
if (int(Num) == 0 and ComNum > 10):
    print("用户赢了")
elif (int(Num) == 1 and ComNum < 10):
    print("用户赢了")
else:
    print("用户输了")