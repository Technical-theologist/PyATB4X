def pizza(*toppigs,base):

    print(toppigs)
    print(base)

pizza("tomato","redpepper","olive",base="Wheat")


def pizza_2(toppigs,*base):

    print(toppigs)
    print(base)
pizza_2("tomato", "redpepper", "olive", base="Wheat")
#mutli args to be placed at the starting of the function
#2 multi args are not allowded