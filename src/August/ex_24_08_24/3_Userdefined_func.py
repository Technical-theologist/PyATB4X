""""
There are 4 types of the user defined func
•They cannot retun -Non return
•They can retur someting
•They have parameter
•They dont have paramenters
"""
#They canot return any thing>-non return type
def greet():
    print("Hello")
result=greet()
print(result)
#Non return type with argument
def greet_by_name(name):
    print(f"Hello {name}")
#No return type with def argument
def greet_say_hello(name="Karthi"):
    print("Hello",name)
greet_say_hello()
greet_say_hello("John")#Positinoal Argument
#Argument and return type
def sum_of_tow_no(a,b):
    return a+b
result=sum_of_tow_no(10, 20)#Keyword Argument

def sub_of_two_no(a=200,b=100):#default argument
    return a-b
print(sub_of_two_no())