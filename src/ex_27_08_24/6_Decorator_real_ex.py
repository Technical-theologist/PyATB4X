import time


def add_before_ui(func):
    def wrapper():#wrapper and call
        print("before the running of the UI TC")
        print("Login the application")
        func()
        print("after the running of the UI TC")
        print("Logout the application")

    return wrapper


@add_before_ui
def testcase_functionality():
    print("Test case running the adding to cart")

def time_decorator(func):
    def wrapper():
        starttime=time.time()
        func()
        endtime=time.time()
        total_time_taken=endtime-starttime
    return wrapper()
def a_new_func():
    print("I am a new function")
    time.sleep(2)
