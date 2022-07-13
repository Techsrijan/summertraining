import math
n=int(input("enetr any number"))
k=math.sqrt(n)
#k=n
i=2
while i<=k:
    if k%i==0:
        print("Not prime")
        break
    i = i + 1
else:
    print("Prime no")

