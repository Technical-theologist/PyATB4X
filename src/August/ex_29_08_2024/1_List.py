# List allow the duplicate data and lis
# is mutable and indexed
# list1=[1,2,"str",10.5]
list = [1, 2, 3]
print(list)
print(len(list))
list[0] = 4
print(list)
list.extend([5,6,7])
print(list)
list.extend(["str","dic"])
print(list)
list.insert(1,10)
print(list)
list.remove("str")
print(list)
list .remove("dic")
print(list)
list.sort()