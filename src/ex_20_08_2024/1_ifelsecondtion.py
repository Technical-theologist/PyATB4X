num1=float(input("Enter the first number: "))
num2=float(input("Enter the second number: "))
if num1>num2:
    print(f"{num1} is greater than {num2}")
else:

    print(f"{num2} is greater than {num1}")

#Grade Caluculator

marks=int(input("Enter the marks"))
if marks>=90:
    print("Grade A")
elif marks>=80:
    print("Grade B")
elif marks>=70:
    print("Grade C")
elif marks>=60:
    print("Grade D")
elif 100>marks:
    print("Cannot be greater than 100")
elif 0>marks:
    print("Cannot be less than 0")
else:
    print("Grade F")
    print("Better luck next time")