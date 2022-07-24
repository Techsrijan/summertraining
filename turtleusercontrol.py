from turtle import *
t=Turtle()
sc=Screen()
def moveleft():
    t.forward(100)

def moveright():
    t.backward(100)

def moveup():
    t.left(90)

def movedown():
    t.right(90)

sc.listen()
sc.onkey(moveleft,'L')
sc.onkey(moveright,'Right')
sc.onkey(moveup,'Up')
sc.onkey(movedown,'Down')
done()