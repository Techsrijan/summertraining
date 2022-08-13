class Theory:
    def a(self):
        print("this is class A")

class Sessional:
    def b(self):
        print("this is class B")

class Result(Theory,Sessional) :
    def msg(self):
        print("this is result")

r=Result()
r.msg()
r.a()
r.b()
