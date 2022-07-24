from turtle import *
t=Turtle()
t.circle(-50)
t.circle(50)
t.write("Hello",font=("comic Sans Ms",25,'bold'))
#t.reset()
#t.undo()
#t.undo()
#t.circle(-500)
t.clear()

t.circle(200,steps=15)
t.clear()
#t.circle(200,180)
t.shape('turtle')
for i in range(5):
    #t.setposition(50,50)
    t.forward(25)
    t.stamp()

done()