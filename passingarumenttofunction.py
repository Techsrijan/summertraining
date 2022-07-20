def person(name,age):  #name and age are formal argument
    print(name)
    age=age+10
    print(age)
'''   
name=input("enetr your name")
age=int(input("enetr your age"))
person(name,age)'''

person("ashwani",22)  # here ashwani and 22 actual argument
#person(22,"ashwani")

person(name="ashwani",age=55)
person(age=22,name="xyz")
