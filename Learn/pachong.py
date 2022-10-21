# class Car:
#     price = 10000
#     def __init__(self,c):
#         self.color = c
# car1 = Car('Blue')
# car2 = Car('Red')
# # print(car1.color,Car.prince)
# ## 修改类的属性
# Car.price = 20000
# ## 增加类的属性
# Car.name = 'Pivix'
# ## 修该实例属性
# car1.color = 'Yellow'
# print(car2.color, Car.price, Car.name)
# print(car1.color, Car.price, Car.name)
# import types
# def setSpeed(self,s):
#     self.speed = s
# #动态为对象增加成员方法
# car1.setSpeed = types.MethodType(setSpeed,Car)
# #调用对象的成员方法
# car1.setSpeed(50)
# print(car1.speed)


# class A:
#     def __init__(self, value1=0, value2=0):
#         self._value1 = value1
#         self.__value2 = value2
#     def setValue(self, value1, value2):
#         self._value1 = value1
#         self.__value2 = value2
#     def show(self):
#         print(self._value1)
#         print(self.__value2)
# a = A(1,2)
# a._A__value2 = 3
# print(a._value1,a._A__value2)
# class Root:
#     __total = 0
#     def __init__(self,v): ## 私有方法
#         self.__value = v
#         Root.__total+=1
#     def show(self): ## 公有方法
#         print('self.__value:',self.__value)
#         print('Root.__total:',Root.__total)
#     @classmethod ## 类方法
#     def classShowTotal(cls):
#         print(cls.__total,Root.__total)
#     @staticmethod ## 静态方法
#     def staticShowTotal():
#         print(Root.__total)
# r = Root(3)
# # 通过对象调用
# r.classShowTotal()
# r.staticShowTotal()
# r.show()
# rr = Root(5)
# Root.classShowTotal()
# Root.staticShowTotal()
# #试图通过类名直接调用实例方法(即公有方法)，失败
# Root.show()
# # 通过类名调用实例方法时为self参数显式传递对象名
# Root.show(rr)
# class Test:
#     def __init__(self, value):
#         self.__value = value
#
#     @property
#     def value(self):  # 只读，无法修改和删除
#         return self.__value
# t = Test(3)
# print(t.value)
# #只读属性不允许修改值
# t.value = 5
# #动态增加新成员
# t.v=5
# print(t.v)
# #动态删除成员
# del t.v
# #试图删除对象属性，失败
# del t.value
# print(t.value)


# class Test:
#     def __init__(self, value):
#         self.__value = value
#
#     def __get_value(self):
#         print('__get_value')
#         return self.__value
#
#     def __set_value(self, v):
#         print('__set_value')
#         self.__value = v
#
#     value = property(__get_value, __set_value)
#
#     def show(self):
#         print(self.__value)
# t = Test(3)
# ## 允许读取属性值
# print(t.value)
# ## 允许修改属性值
# t.value = 5
# print(t.value)
# t.show()
# #试图删除属性，失败
# del t.value


