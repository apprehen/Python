import string
test_str='good,bad.,haha!oh????en.heihei#well@4'
result=[]
word=[]
biaodian=string.punctuation+' '
for ch in test_str:
    if ch in biaodian:
        if word!=[]:
            result.append(''.join(word))
            word=[]
    else:
        word.append(ch)
if word!=[]:
    result.append(''.join(word))
print result



import re
print re.split('[,.?#@! ]+',test_str)
print re.findall('[a-zA-Z0-9]+',test_str)

