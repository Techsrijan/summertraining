from numpy import *
arr=array([1,2,3,4,5,6])
arr2=arr  #aliasing
print(arr,"address=",id(arr))
print(arr2,"address=",id(arr2))

arr[0]=1000
print(arr,"address=",id(arr))
print(arr2,"address=",id(arr2))

# what if u want two different address
arr3=array([1,2,3,4,5,6])
arr4=arr3.view()  #shallow copy
print(arr3,"address=",id(arr3))
print(arr4,"address=",id(arr4))

arr3[0]=1000
print(arr3,"address=",id(arr3))
print(arr4,"address=",id(arr4))


# what if u want two different address and changes of anyone doest not affect other
arr5=array([1,2,3,4,5,6])
arr6=arr5.copy()   #deep copy
print(arr5,"address=",id(arr5))
print(arr6,"address=",id(arr6))

arr5[0]=1000
print(arr5,"address=",id(arr5))
print(arr6,"address=",id(arr6))
