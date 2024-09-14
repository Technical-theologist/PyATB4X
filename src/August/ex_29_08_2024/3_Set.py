#SET- Collection of the unique values and unordered
set_1={1,2,2}
print(set_1)# o/p-1,2
#in real time it is used to remove the duplcate value in list
list1=[2,5,8,9,10,9,10]
set_2=set(list1)
print(set_2)
set_3=set_1.union(set_2)
print(set_3)
set_4=set_1.intersection(set_2)
print(set_4)
#remove the duplicate in set 1 a,d set2
set_5=set_1.difference(set_2)
print(set_5)
#subset is used to check every element is present in the main set
set_6=set_2.issubset(set_1)
print(set_6)
set7=set_2.add(11)
print(set7)