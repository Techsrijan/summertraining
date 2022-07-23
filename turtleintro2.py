from turtle import *
t=Turtle()

def shape():
    for i in range(3):
        t.forward(100)
        t.left(90)

shape()
t.fd(200)
t.left(25)
t.fd(500)
t.backward(700)
shape()
done()