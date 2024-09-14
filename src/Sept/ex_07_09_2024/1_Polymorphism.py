#one can have many forms
#we can achive by over loading or overriding
#Method OVerriding-Child or subclass can have same
#method as the parent or superclass
#you can over ride the method of the parent class
#in below case there are "area"method in each class
#the area method got overrided when the object is instanciated

class Shape:
    def area(self):
        print("Area of a shape")
class Rectangle(Shape):
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        return self.length*self.breadth

class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return 3.14*self.radius*self.radius

shape1=Rectangle(10,20)
print(shape1.area())
shape2=Circle(10)
print(shape2.area())

class Father:
    def house(self):
        print("I have 2BHK house")
class Son(Father):
    def house(self):
        print("I have 3BHK House")
kar=Son()
kar.house()

#Ex with super class
class Father:
    def house(self):
        print("I have 2BHK house")
class Son(Father):
    def house(self):
        super().house()#it will call the father house also
        print("I have 3BHK House")
kar=Son()
kar.house()
