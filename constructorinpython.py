'''
constructor is a special member function which invoked automatically
when the object of this class is created.
'''

class Test:
    def msg(self):
        print("Is it poosible to run this function without object")
    def __init__(self):  #constructor
        print("yes it is possible")

t=Test()
t2=Test()
t.msg()
t2.msg()