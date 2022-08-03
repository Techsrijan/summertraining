from tkinter import *

root=Tk()
def getdata():
    print(i.get())
    print(j.get())

l=LabelFrame(root,text="Select Language Known")
i=IntVar()
r1=Checkbutton(l,text="Hindi",variable=i)
j=IntVar()
r2=Checkbutton(l,text="English",variable=j)
r1.pack()
r2.pack()
l.pack()

btn2 = Button(root, text="getdata",
                font=("comic Sans Ms", 10, "bold"), fg="green", command=getdata)
btn2.pack()
root.geometry("600x800+120+300")
#root.resizable(0,0)
root.mainloop()