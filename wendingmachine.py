stock=20
n=int(input("how many toffe u want"))
i=1
while i<=n:
    if i<=stock:
        print("Collect toffe=",i)

    else:
        print("Out Of stock")
        break
    i=i+1
else:   #this else will run when loop runs properly
    print("thank u please visit again")
