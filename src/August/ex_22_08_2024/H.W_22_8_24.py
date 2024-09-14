# Task-9 FizzBuzz Test: Write a program that prints numbers from 1 to 100. #
# Loop For However, for multiples of 3, print "Fizz" instead of the number,
# and for multiples of 5, print "Buzz."
# For numbers that are multiples of both 3 and 5, print "FizzBuzz."

for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)

# Task-10: Print the factorial
number = int(input("Enter a number: "))
factorial = 1
if number < 0:
    print("Factorial does not exist for negative numbers")
else:
    """"
    factorial =it multiply the number upto the 
    1
    factorial=1*1=1
    factorial=1*2=2
    factorial=2*3=6
    factorial=6*4=24
    factorial=24*5=120
    """
    for i in range(1, number + 1):
        factorial = factorial * i
    print(f"The factorial of {number} is {factorial}")
# Fabinochi series
# 0 1 1 2 3 5 8 13
number = int(input("Enter the number: "))
n, m = 0, 1

for i in range(number):
    if n == number:
        print("Number is in the Fibonacci series")
        break
    n, m = m, n + m
else:
    print("Number is not in the Fibonacci series")
