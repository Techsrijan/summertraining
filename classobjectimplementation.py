class Student:
    def msg(self):   #self is the object of class which is passed automatically
        print("hello")

    def student_info(self,name,age):
        self.name=name
        self.age=age
        print("Name=",self.name)
        print("age=",self.age)

s=Student()  #creating object of student class
Student.msg(s)  # what is s-object-self

s.msg()
s.student_info("ashwwani",11)
