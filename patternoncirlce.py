from turtle import *
t=Turtle()
'''
t.pu()
t.goto(100,100)
t.pd()
t.circle(-50)
'''
l=['red','blue','orange','yellow','green']
t.pu()
t.forward(300)
t.pd()
t.pensize(20)
for i in range(5):
    t.pencolor(l[i])
    t.circle(50)
    t.pu()
    t.backward(100)
    t.pd()


done()