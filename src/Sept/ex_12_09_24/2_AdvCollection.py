#Basic data structure
"""
1.List
2.Tuple
3.Set
4.Dict
"""
#Advance Collections
"""
1.deque-Queue
2.defalut Dict
3.Counter
4.OrderedDict
5.ChainMap
6.Named Tuple
generally we use the deque and OrderedDict"""
#Deque-double ended q
from collections import deque
#d=deque()
d=deque([1,2,3])
print(d)
d.append(4)
print(d)
d.appendleft(0)
d.extend([5,6])#extend is equivalent to append but it append more than 1 item
print(d)

#order dict
#it remember how u insert
from collections import OrderedDict
a={"name":"ksk","age":"22","id":"123"}
print(a)