#utf-8

x = input('输入一个三位数')
x = int(x)
bw = x//100
gw = x % 10
sw = x//10%10
print("百位：%d, 十位:%d, 个位:%d" % (bw, sw, gw))