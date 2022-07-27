'''
Types of Methods in Python
Instance methods
Class methods
Static methods
Decorators are a very powerful and useful tool in Python since
 it allows programmers
to modify the behaviour of a function or class.
'''

class Student:
    school="Techsrijan"
    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3

    def total_marks(self):
        return (self.m1+self.m2+self.m3)

    @staticmethod  # decorator
    def msg(m, n):
        print(m + n)
        print("this will run without any object")
    @classmethod   #decorator
    def school_name(cls):
        return cls.school

s1=Student(10,20,30)
print(s1.total_marks())

Student.msg(67,68)
s1=Student(10,20,30)
print(s1.total_marks())

print(Student.school_name())

