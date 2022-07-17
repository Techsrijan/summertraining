from array import *
arr=array('i',[])
n=int(input("how many students u have"))

for i in range(n):
    x=int(input("enetr the marks of student"))
    arr.append(x)


print(arr)

for i in arr:
    print(i)

search=int(input("enetr the marks u want search"))
# python built in function
print("Value mila=",arr.index(search))


ind=0
for k in arr:
    if k==search:
        print("Item found",ind+1)
        break
    ind=ind+1
    k=k+1
else:
    print("item not found")

