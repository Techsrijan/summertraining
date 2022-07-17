#import array
from array import *

a=array('i',[4,5,6,7,8,8])

print(a)

print(a.buffer_info())

for i in a:
    print(i)

for i in range(len(a)):
    print(a[i])


print(a.reverse())
print(a)