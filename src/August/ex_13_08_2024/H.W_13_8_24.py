# Taks 1

table=9
print("Multiplication table of",table)
print(f"{table}*1={table*1}")
print(f"{table}*2={table*2}")
print(f"{table}*3={table*3}")
print(f"{table}*4={table*4}")
print(f"{table}*5={table*5}")
print(f"{table}*6={table*6}")
print(f"{table}*7={table*7}")
print(f"{table}*8={table*8}")
print(f"{table}*9={table*9}")
print(f"{table}*10={table*10}")


for i in range(1,10+1):
    print(f"{table}*{i}={table*i}")
# Task2
"""diff functions under the int 
sum(),*,/,-,pow(),
To round the values you can use the .f function"""
x=int(input("enter the input values of x"))
y=int(input("enter the input values of y"))
quotient = x / y
print(x+y)
z=sum([4,8])
print(z)
print(x-y)
print(x*y)
print(x/y)
print(pow(x,y))
print(f"{quotient:3f}")
print(2**3)
print(x^y)

# Task 3
""""
a)Diff b/w the = operator and == operator
    The main diff b/w the = and == is assignment operator and the comparison operator
    int x=10(you are assigning the integer of x variable for 10
    "if(x==y)
        print(x+y)"
    here we are comparing if x=y then print x+y
b)what does the ** operator do in python and how it is used
    it is used to do power of a number 
    ex- print(2**2) =o/p- 4
        print(2**3) =o/p- 8
c) what does the ^ operator do in python and what does it commonly used for
    it split the number into its binary form
    and the ^ operator is used to do the swapping of the numbers
    let say  x=10 and y=20
    x=x^y
    y=x^y
    x=x^y
    now the value of x=20 and y=10
    """








