x=10
def fun():
    x=8
    global y
    y=12
    print("local=",x)
    p=globals()['x']
    print("global access inside local=",p)


fun()
print("global=",x)
print("Localglobal=",y)

