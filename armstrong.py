n=int(input("enetr any number"))
orig=n
sum=0
mul=1
while n>0:
    digit=n%10
    sum=sum+digit
    mul = mul * digit
    n=n//10
print("sum=",sum)
print("mul=",mul)
print("n=",n)
if mul==sum:
    print("magic number")
else:
    print("Not ")