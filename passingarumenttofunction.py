'''
We can pass value inside function by four methods
1. positional arguments
2. keyword argument
3  variable length argument
4. keyword variable length argument
'''

def person(name,age):  #name and age are formal argument
    print(name)
    age=age+10
    print(age)
'''   
name=input("enetr your name")
age=int(input("enetr your age"))
person(name,age)'''

#1. positional arguments
person("ashwani",22)  # here ashwani and 22 actual argument
#person(22,"ashwani")

#2. keyword argument
person(name="ashwani",age=55)
person(age=22,name="xyz")


def add1(x,y):
    c=x+y
    print(c)

add1(3,5)

#3  variable length argument

def add(x,*y):
    print(x)
    print(y)
    s=x
    for i in y:
        s=s+i
    print("Sum=",s)

add(3,6,7,8,9,4,6,56,7,8,4,8,6)

def add2(*y):
    s = 0
    for i in y:
        s = s + i
    print("Sum=", s)
add2(3,6,7,8,9,4,6,56,7,8,4,8,6)


#4. keyword variable length argument

def personData(name,**data):
    print(name)
    print(data)
    for i,j in data.items():
        print(i,j)
        #print(j)

personData(name="abc",age=25,city="gkp",mob=9956477677)