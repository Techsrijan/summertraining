class Car:
    country="India"  #instance variable # static variable
    def milage(self,mil):
        self.mil=mil
        print(self.mil)

    def name1(self):
        self.name = "maruti"  # local vaiable
        print(self.name)
c1=Car()
print(c1.country)
c1.milage(52)
c1.name1()
c2=Car()
c2.country="America"
print(c2.country)
print(c1.country)
print(Car.country)
Car.country="china"
print(Car.country)