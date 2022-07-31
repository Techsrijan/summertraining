from tkinter import *
from tkinter import messagebox
root=Tk()


def msg():
  wn=Toplevel(root)
  wn.title("Top Window")
  btn2 = Button(wn, text="Close",
                font=("comic Sans Ms", 15, "bold"), fg="green", command=wn.destroy)
  btn2.pack()
  wn.geometry("600x400+600+300")


btn3=Button(root,text="Open New window",
           font=("comic Sans Ms", 15, "bold"), fg="green",command=msg)
btn3.pack()

btn1 = Button(root, text="Close",
              font=("comic Sans Ms", 15, "bold"), fg="green", command=quit)
btn1.pack()
root.geometry("600x400+600+300")
root.resizable(0,0)
root.mainloop()