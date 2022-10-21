#根据上面的步骤完成代码
fp = open('students.txt', 'rt', encoding='utf-8')
content = fp.readlines()
fp.close()

idnums = []
names = []
for line in content:
    items = line.strip().split(',')
    idnums.append(items[0])
    names.append(items[1])
    
# attendance 存放考勤数据,填写考勤数据
attendances = [0] * len(idnums)    # 假设填写所有人都没到

print("请输入到课情况，到课请输入1，未到请输入0")
for i in range(len(idnums)):
    ans = input("学号:%s    姓名：%s   到课情况：" % (idnums[i], names[i]))
    attendances[i] = int(ans)

#构造考勤数据文件名
from datetime import datetime
fname = datetime.now().strftime('attendance_%Y-%m-%d.txt')

#写入考勤数据到文件，执行完成后，查看写入的文件
fp = open(fname, 'wt', encoding='utf-8')
for idnum,name,attendance in zip(idnums, names, attendances):
    line = "%s,%s,%d" % (idnum, name, attendance)
    print(line, file=fp)
fp.close()