#oops-Object oriented program-

#procedural programing language-
#Every thing you create you can divide into functions'
#its not that close to the real world
#productivity is low in the procedural programing lang

class man:
    #Attributes
    age=None
    height=None
    colour=None
    name=None

    #Behaviour
    def talk(self):#No return type with no argument This self is the first argument in every behaviour
        print("I can talk")
    def walk(self,name):#Argument with return type
        print("I can walk",name)

    def sleep(self,age):#Argument with return type
        print("I am a method")
        return None
    def back(self):#No argument with return type
        return None

karthik=man()#Karthik is object
karthik.name="kart"
print(karthik.name)

xyz=man()
xyz.height=6.0
print(xyz.height)
#no one is there to set the value of the karthik.name
# we have to set the value everytime to eleminate this we
# will use the constructor
