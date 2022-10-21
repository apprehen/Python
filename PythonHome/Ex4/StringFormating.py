# -*- coding: cp936 -*-
print 'The number {0:,} in hex is: {0:#x}, the number {1} in oct is {1:#o}'.format(5555,55)
print 'The number {1:,} in hex is: {1:#x}, the number {0} in oct is {0:#o}'.format(5555,55)


print 'my name is {name}, my age is {age}, and my TelNumber is {tel}'.format(name = "Dong Fuguo",age = 37,tel = '13853516964')


position = (5,8,13)
print 'X:{0[0]};Y:{0[1]};Z:{0[2]}'.format(position)


weather = [('Monday','rain'),('Tuesday','sunny'),('Wednesday','sunny'),('Thursday','rain'),('Friday','Cloudy')]
formatter = "Weather of '{0[0]} is '{0[1]}'".format
for item in map(formatter,weather):
    print item


#map用法扩展
s = '2014-10-31'
t=s.split('-')
print t
print map(int,t)
