from tkinter import *
from PIL import Image, ImageTk


root=Tk()
can=Canvas(root,width=500,height=600,bg="yellow")
can.pack()
line=can.create_line(0,0,500,600,fill="red",width=5)
line2=can.create_line(0,600,500,0)
cir=can.create_oval(100,100,200,200,fill="green")
oval=can.create_oval(200,200,300,400,fill="red")

rec=can.create_rectangle(100,100,200,200)
arc=can.create_arc(100,100,200,200,fill="yellow",extent=-180)
# Load the image
img=ImageTk.PhotoImage(file="TCS1.jpg")
#photo=PhotoImage(file="TCS1.jpg")
can.create_image(0,0,image=img,anchor=CENTER)

points=[250,110,480,200,280,280,250,110]

poly=can.create_polygon(points,fill="blue",outline="white",width=5)
root.geometry("800x600+120+120")

root.mainloop()