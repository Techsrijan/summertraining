from turtle import *
t=Turtle()
l=['red','blue','orange','yellow','green']
for i in range(200):
    t.pencolor(l[i%5])
    t.pensize(i/10)
    t.forward(i)
    t.left(59)
done()