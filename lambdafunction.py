from functools import reduce
def add(x,y):
    return x+y

print(add(4,6))

'function without name--anonymous function '

f=lambda x,y:x+y

print(f(5,6))

#filter, map and reduce
l=[2,3,5,6,883,87,99]
print(l)
def is_even(n):
    return n%2==0

even=list(filter(lambda n:n%2==0,l))
print(even)

#map

op=list(map(lambda n:n+5,even))
print(op)

#reduce
finalop=reduce(lambda a,b:a+b,op)
print(finalop)



