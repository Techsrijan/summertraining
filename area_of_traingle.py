#import math  #this is single line comment
'''
mbmdsbf
fdsfklsd
this is multiline comment
'''
#import math as m
#from math import *  # most usable
from math import sqrt
a,b,c=4,5,6
s=(a+b+c)/2
#area=math.sqrt(s*(s-a)*(s-b)*(s-c))
#area=m.sqrt(s*(s-a)*(s-b)*(s-c))
area=sqrt(s*(s-a)*(s-b)*(s-c))
print("Area=",area)
