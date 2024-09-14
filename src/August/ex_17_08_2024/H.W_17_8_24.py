#Task4- Write a program to calulate the area of the circle
radius=int(input("radius of the circle in cm's"))
area=3.14*radius**2
print(area)

#Task5-Create a program to take 2 no as input  and prints whether the first no is greater than,
# less than or equal to the second no
num1=int(input("Enter the first number"))
num2=int(input("Enter the second number"))
if num1>num2:
    print(f"{num1} is greater than {num2}")
elif num1<num2:
    print(f"{num2} is greater than {num1}")
else:
    print(f"{num1} is equal to {num2}")
#Task6-Caluculate the square and cube of the given number
num=int(input("Enter the number"))
square=num**2
cube=num**3
print(square,cube)

