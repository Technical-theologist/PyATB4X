"""The constructor is used to instanciate the class
1.Without the constructor if we call the class
  we wont able to return or get the values
2.if we pass the paramenter or attribute to the constructor
  it will be used in the function/method also
"""
#default constructor
class def_const():
    def __init__(self):#you are not passing additional parametner ie default constructor
        self.name="Karthikeya"
    def person(self):
        print("he is learning",self.name)

detail=def_const()
detail.person()


