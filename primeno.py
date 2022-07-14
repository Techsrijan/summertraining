#import math
from math import *
n=int(input("enetr any number"))
k=(sqrt(n))
print(k)

i=2
while i<=k-1:
    if k%i==0:
        print("Not prime")
        break
    i = i + 1
else:
    print("Prime no")
print("thank you")
