# Decorator-Decorator in puthon used to
""""modify the behaviour of the function or class without
    changing the source code
    They are powerful tool that allow to wrap another function
    and extends its functionality while keeping the source code
    unchanged
Benifits of the using decorators=
    Code Reusablitlity-Decorators allow you to reuse
    the same functionality across multiple fucntions
Saperation of Concerns-Theny help in saperating the core
    logic of functions from auxilary concerns like
    logging acess control etc
Enhcance Readability-Decorators can make the code more
    readable and easier to understand
"""


def my_decorator(func):
    def wrapper():
        print("Before the function is called")
        func()#drive_bike() function is called here
        print("After the function is called")

    return wrapper()


@my_decorator#declaring or defining the decorator function
def drive_car():
    print("I am driving a car")
@my_decorator
def drive_bike():
    print("I am driving a bike")


