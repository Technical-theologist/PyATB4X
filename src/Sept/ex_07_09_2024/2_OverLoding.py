# Method over loding
# Method over loading is not supported in the python
"""class summation(object):
     def sum(self,a,b):
         return a+b
     def sum(self,a,b,c):#the values of the a,b,c& above has a,b so
         #python will get confused to which one to call
         return a+b+c
adding=summation()
adding.sum(10,20)"""


# how to call it
class summation(object):  # is A object -single inheritence
    def sum(self, a, b):
        return a + b

    def sum(self, a, b, c=0):  # the values of the a,b,c& above has a,b so
        # python will get confused to which one to call
        return a + b + c


adding = summation()
adding.sum(10, 20)
print(adding)
