print(range(10))
print(range(0,10))
for i in range(10):
    print(i)

for i in range(1,10):
    print(i,end="")
print()
for i in range(1,10,2):
    print(i,end="")

a,b=25,12
if a<b:
    for i in range(a,b):
        if i%2==0:
            print("even=",i,end="")
        else:
            print("odd=", i)
else:
    for i in range(a,b,-1):
        if i%2==0:
            print("even=",i,end="")
        else:
            print("odd=", i)