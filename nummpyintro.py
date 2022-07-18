from numpy import *
arr=array([11,3,4,66,8])
print(arr)
print(arr.dtype)
print(arr.ndim)
'''
there are 6 ways to create any arry using numpy
1. array
2. linspace
3. logspace
4. arange
5. zeros
6. ones
'''

arr2=linspace(1,50,100)
print(arr2)

arr3=logspace(1,50)
print(arr3)

arr4=arange(1,15,2)
print(arr4)

arr5=zeros(5)
print(arr5)

arr6=ones(5,int)
print(arr6)