fp = open('C:/Users/35143/Desktop/PythonHome/Hw3/students.txt', 'rt', encoding='utf-8')
content = fp.readlines()
# print(content)
fp.close()
idnums = []
names = []
for line in content:
    items = line.strip().split(',')
    idnums.append(items[0])
    names.append(items[1])
# print(idnums, names)
attendances = [1] * len(idnums)    # 假设填写所有人都到了
attendances
from datetime import datetime
fname = datetime.now().strftime('attendance_%Y-%m-%d.txt')
fp = open(fname, 'wt', encoding='utf-8')
for idnum,name,attendance in zip(idnums, names, attendances):
    line = "%s,%s,%d" % (idnum, name, attendance)
    print(line, file=fp)
fp.close()



