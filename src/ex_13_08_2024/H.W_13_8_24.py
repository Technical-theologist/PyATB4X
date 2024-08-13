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







