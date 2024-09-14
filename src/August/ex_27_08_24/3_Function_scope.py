#Function scope has the Global and local scope
global_int=30
def function():
    local_int=20
    print(global_int)
    print(local_int)

function()

#Fucntion_withinfucntion
def function_1():
    x=10
    print(x)
    def function_2():
        print(x)
    function_2()

function_1()
