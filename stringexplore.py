
st="welcome to Python to Programming"
print(len(st))
print(st.upper())
print(st.lower())
print(st.capitalize())
print(st.swapcase())
print(st.title())
print(st.count('to'))
print(st.split(','))
for i in st.split( ):
    print(i)
'''
print(st.endswith('t'))
name=input("enetr your name")
print(name)
if name.isalpha():
    print(name)
else:
    print("Sahi sahi input karo")

phone=input("enter your contact no")
if phone.isdigit():
    print(phone)
else:
    print("invalid phone no")

enroll=input("enter enrollment no")
if enroll.isalnum():
    print(enroll)
else:
    print("invalid")

para="Her name is tamanna and tamanna is good girl"
search=input("enter the text u want to search")
if para.find(search)==-1:
    print('data nahi mila')
else:
    print('koi mil gaya')
if search in para:
    print("Item found")
    rep=input("Item u want to replace with")
    x=para.replace(search,rep)
    print(x)

else:
    print("Item not found")


print(para.find(search))'''

xt="       hello Brother       "
print(xt,end="")
print("hello bhai")

print(xt.rstrip(),end="")   #change strip and lstrip
print("space hat gaya")



tt="!!!!!!!!!hello Brother       "
print(tt,end="")
print("hello bhai")

print(tt.strip('!'),end="")   #change strip and lstrip
print("space hat gaya")


