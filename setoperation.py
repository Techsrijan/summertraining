s={}
print(type(s))
t=set()
print(type(t))

'''
q=eval(input("enter the elements of set"))
print(q)

d={2,3,5,7,8,99}
print( 3 in d)
print( 30 in d)
print(d)
d.add(500)
print(d)

d.remove(7)
print(d)
'''

a={1,2,3,4}
b={6,4,8,9}
print(a|b)  #union

print(a&b) #intersection

print(a-b) # which are in a but not in b

#symmetric difference
print(a^b) # not common a and b