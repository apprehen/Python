print('111')
#输出含有运算符的表达式
print('Hello'+'World')
print(3+5)
#将数据输入到文件中,/表示系统盘的位置捏
fp = open('C:/Users/35143/Desktop/text.txt','a+')
print('HelloWorld',file=fp) #不存在就创建，存在就追加
fp.close()