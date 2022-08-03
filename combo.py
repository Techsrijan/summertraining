from tkinter import *
from tkinter.ttk import Combobox
root=Tk()
def getdata():
    print(c.get())
l=[1,2,3,4,5,6,7]
c=Combobox(root,values=l)
c.set('SELECT DATE')
c.pack()
btn2 = Button(root, text="getdata",
                font=("comic Sans Ms", 10, "bold"), fg="green", command=getdata)
btn2.pack()
root.geometry("600x800+120+300")
#root.resizable(0,0)
root.mainloop()