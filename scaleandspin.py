from tkinter import *

root=Tk()
def getdata():
    print(i.get())
    print(sp.get())

i=IntVar()
s=Scale(root,from_=100, to=500,orient='horizontal',sliderlength=40,length=200,variable=i)
s.pack()


sp=Spinbox(root,from_=1,to=5)
sp.pack()

btn2 = Button(root, text="getdata",
                font=("comic Sans Ms", 10, "bold"), fg="green", command=getdata)
btn2.pack()
root.geometry("600x800+120+300")
#root.resizable(0,0)
root.mainloop()