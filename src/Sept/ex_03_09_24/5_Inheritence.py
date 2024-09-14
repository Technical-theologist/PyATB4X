#Single Inheritence

class Basic_car:
    structure="frame"
    def tyres(self):
       print("4 tyres")

class Moderncar(Basic_car):
    pass
bmw=Moderncar()
print(bmw.structure)


#Multiple Inheritence
class name:
    person="A"
    home="2BHK"
class age:
    age="10-100"
    home="3BHK"
class person(name,age):#two class in one class and
    # if the parameters have same name such as "home"in
    # this case then first one or first class will be called in object
    #this is know as diamond problem we had solved in python but not in java
    pass

amit=person()
print(amit.age)
print(amit.home)

#MultiLevel Inheritnece
class grand_father:
    print("I will give doc to my son")
class parent(grand_father):
    pass
class son(parent):
    pass

person_1=son()
person_1

