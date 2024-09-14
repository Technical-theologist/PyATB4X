""""
class variable
Method
    1.Public-Dont mention anything
    2.Protected
    3.Private
Inheritance
Polymorphism
Abstraction
Encapsulation
Static Method
Variables"""


# Variable=
# 1.Local Variable(within the class)
# 2.Global Variable(outside of the class)
# 3.Instance Variable(within the class)
# 4.Static Variable
# Local Variable
class local_var:
    def local_var1(self):
        a = 10  # you had provided a paramemter inside a function ie local variable
        print(a)


x = local_var()
x.local_var1()
# Global Variable
b = 20  # you provided a parameter outside a class


class global_var:
    def global_var_1(self):
        print(b)


y = global_var()
y.global_var_1()


# Instance Variable-you have to instanciate the value of the variables

class instance_var():
    def instace_var_1(self, c, d):
        return c + d


c = int(input("provide the value of c"))
d = int(input("provide the value of d"))
sum = instance_var()
result = sum.instace_var_1(c, d)
print(result)

#
