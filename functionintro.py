#function definition
#how to declare a function
def baris():
    print("Kab barsoge")

#function call
baris()
baris()
baris()


def greet():
    print("good Morning")

greet()
baris()
greet()


def add():
    a,b=5,6
    c=a+b
    print(c)

add()

def add1(x,y):  #here x and y are call argument or parameter
    c=x+y
    print("sum=",c)

add1(5,8)

p=int(input("Enetr First number"))
q=int(input("enter Second number"))

add1(p,q)

# function with return a value
def square(x):
    d=x*x
    cube=x*x*x
    return d,cube



s,t=square(25)
print(s,t)
print("Square of this=",s)
print("cube=",t)