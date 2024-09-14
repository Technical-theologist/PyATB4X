#there are so many types of the exception are there
#run time error, over flow error,index error

num1=int(input("Enter the number1"))
num2=int(input("Enter the number2"))
div= num1/num2
print(div)
# if u enter the num 1 string then Value error will come
#if u enter the num1 as 10 and num2 as 0 then ZeroDivisionError will come
try:
    num1=int(input("Enter the number1"))
    num2=int(input("Enter the number2"))
    div= num1/num2
    print(div)
except ValueError as Va:
    print("Enter the number instead of string")
except ZeroDivisionError as zd:
    print("num 2 cannot be zero")
finally:print("Always executed after try except block")
