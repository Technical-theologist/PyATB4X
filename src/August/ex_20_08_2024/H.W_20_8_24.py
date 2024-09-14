#Task 7 -Leap year caluculation
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

#or
year = int(input("Enter a year: "))
if (year%4==0 and year%100!=0):
    print(f"{year} is a leap year.")
elif (year%400==0):
    print(f"{year} is a leap year.")
else:
    print("Provide the correct year number")

#Task8-write a program that classifies the traigle based on its lengths,determine the side
#and print weather its a equilateral or isosceles or scalene triangle
side1=float(input("Enter the length of side 1: "))
side2=float(input("Enter the length of side 2: "))
side3=float(input("Enter the length of side 3: "))
if(side1==side2==side3):
    print("The triangle is equilateral")
elif(side1==side2 or side2==side3 or side1==side3):
    print("The triangle is isosceles")
else:
    print("The triangle is scalene")



