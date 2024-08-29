#LAmbda function=A lambda is a anonymus function
#that returns some form of the data
import math

#def triple_me(num):
#    return num*3
#print(triple_me(4))

o=lambda num:num*3
print(o(4))

oo=lambda num1:int(input("Enter the number:"))*3
print(oo(num1=10))

x=lambda a,b,c:a+b+c
print(x(10,20,30))

b=lambda num:"Even"if (num%2)==0 else "Odd"
print(b(10))
