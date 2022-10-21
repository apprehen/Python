class Rectangle:
    __tatal = 0
    def __init__(self,length,width):
        self.length = length
        self.width = width
        self.__tatal+=1
    def area(self):
        Rectare = self.width * self.length
        return Rectare
    def setwidth(self,w):
        self.width = w
    def setlength(self,l):
        self.length = l
    def show(self):
        print('Width',self.width)
        print('Length',self.length)

# r1 = Rectangle(2,4)
# print(r1.area())
# r1.show()
# r1.setwidth(4)
# r1.setlength(6)
# r1.show()

class Cuboid(Rectangle):
    def __init__(self,length,width,height):
        self.length = length
        self.width = width
        self.height = height
    def volume(self):
        v = self.height*self.width*self.length
        return v
    def show(self):
        print('Width',self.width)
        print('Length',self.length)
        print('Height',self.height)
v1 = Cuboid(2,3,4)
print(v1.volume())
v1.show()
