from turtle import *
t=Turtle()  # t is the object of turtle class
s=Screen()
s.title("My Turtle")
#s.bgcolor('black')
s.bgpic('test.gif')
t.shape('turtle')
t.hideturtle()
t.pencolor('red')
t.fillcolor('yellow')
#t.color('red')
t.speed(1)
t.fillcolor('orange')
t.begin_fill()
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.end_fill()
t.penup()
t.fd(100)
t.pendown()
t.fd(100)
'''
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)'''
for i in range(3):
    t.left(90)
    t.forward(100)
done()