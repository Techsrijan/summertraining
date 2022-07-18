from numpy import *
arr=array([
    [1,2,3],
    [3,3,3],
    [4,4,4],
    [5,6,8]
])
print(arr)
print(arr.ndim)
print(arr.shape)
print(arr.size)
print(arr.flatten())
print(arr.reshape(3,4))


print(arr.reshape(2,2,3))

