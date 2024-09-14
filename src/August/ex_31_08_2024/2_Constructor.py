#It will automatically called when you create the object

class dog():
    name=None
    def sleep(self):
        print("Sleeping")
dog1=dog()
dog1.sleep()#o/p is sleeping instead of dog1.sleep

#we can use the constructor

class dog_2():
    def __init__(self):
        print("It is used when we automatically initieate the object")
    def sleep(self):
        print("Sleeping")
dogy=dog_2()#o/p-It is used when we automatically initieate the object
dogy.sleep()

#ex-3 with None attribute
class cow():
    name=None
    def __init__(self):#Default constructor
        print("This is first cowT")
    def chewing(self):
        print("I will chew")

gauri=cow()#This is first cow
gauri.chewing()#I will chew


# ex-4= With the attribute
class sheep():
    def __init__(self,name):#parametarized constructor
        print("Mehehe")
        self.name=name
    def black_sheep(self):
        print("I will eat htrones")

xyz=sheep("red")
xyz.black_sheep()
print(xyz.name)


class man():
    def __init__(self, name):  # there is name arg is passed along with constructor
        self.name = name
        print("He is tall", name)


karthikeya = man("karthikeya") # "He is tall