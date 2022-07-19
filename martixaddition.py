from numpy import *
a=array([
    [1,2,3],
    [3,3,3],
    [4,4,4],
    [5,6,8]
])
print(a)

b=array([
    [1,2,3],
    [3,3,3],
    [4,4,4]

])
print(b)
print(diagonal(b))
#c=a+b
#print(c)

print("multiplication")
e=a@b
d=dot(a,b)
print(d)

print("mul")
print(e)
