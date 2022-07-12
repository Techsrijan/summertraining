a=int(input("enetr the marks of subject1"))
b=int(input("enetr the marks of subject2"))
c=int(input("enetr the marks of subject3"))
d=int(input("enetr the marks of subject4"))
e=int(input("enetr the marks of subject5"))

total=a+b+c+d+e
per=(total/500)*100

print("Total",total)
print("Percentage=",per)

if per<33:
    print("Fail")

elif per>=33 and per<45:
    print("third division")
elif per>=45 and per<60:
    print("second division")
elif per>=60:
    print("First division")
