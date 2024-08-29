#Loop
#Repeatt a perticluar block of the code multiple times
"""""
For loop-for varialbe in range(Start,stop,step)
if the code that has to be executed multiple times
range(0,10,1)#all are same
range(0,10)#all are same
range(10)#all are same
Break
Continue
"""""
x=list(range(1,11,2))
print(x)
#if you want your list in a strignt line
#use the end deault end has \n (ie next line)
#you can use any thing
for i in range(1,11):
    print(i,end=" ")

for x in range(10,0,-2):
    print(x, end="\n")
