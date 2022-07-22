'''
when a function call itself it is called recursion.
'''
import sys
print(sys.getrecursionlimit())
sys.setrecursionlimit(sys.getrecursionlimit()+2000)
i=0
def greet():
    global i
    print("Good Morning",i)
    i=i+1
    greet()


greet()