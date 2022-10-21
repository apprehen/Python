def crypt(source, key): #source是要加密或解密的字符串，key是密钥字符串
    result = ''
    index = 0
    for ch in source: #遍历字符串中的每个字符
        if index == len(key): #循环使用密钥字符串中的每个字符
            index = 0
        result = result + chr(ord(ch) ^ ord(key[index])) #异或运算
        index = index + 1
    return result

#也可以写成下面更简洁的形式 
def crypt1(source, key):
    from itertools import cycle
    result = ''
    temp = cycle(key)
    for ch in source:
        result = result + chr(ord(ch) ^ ord(next(temp)))
    return result

source = 'Shandong Institute of Business and Technology'
key = 'Dong Fuguo'

print('Before Encrypted:'+source)
encrypted = crypt1(source, key)
print('After Encrypted:'+encrypted)
decrypted = crypt1(encrypted, key)
print('After Decrypted:'+decrypted)
