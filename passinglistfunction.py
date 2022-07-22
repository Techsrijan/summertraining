l=[1,4,2,3,77,5,99]
def passlist(l):
    sum_even=sum_odd=0
    for i in l:
        if i%2==0:
            sum_even=sum_even+i
        else:
            sum_odd=sum_odd+i
    print("Sum of Even=",sum_even)
    print("Sum of Odd=",sum_odd)

passlist(l)