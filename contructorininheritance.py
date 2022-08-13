class Theory:
    def __init__(self):
        print("this is class A")

class Sessional:
    def __init__(self):
        print("this is class B")
class Result(Sessional,Theory) :
    def __init__(self):
        print("ab kya hoga")
    def msg(self):
        print("this is result")

r=Result()
r.msg()

