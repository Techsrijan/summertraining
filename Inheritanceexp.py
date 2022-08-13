class Room:    #base parent
    def area(self,l,b):
        self.l=l
        self.b=b
        print("area=",self.l*self.b)

class GuestRoom(Room):  #child derived
    def msg(self):
        print("This is guest room")


r=Room()
r.area(8,5)

g=GuestRoom()
g.msg()
g.area(5,9)