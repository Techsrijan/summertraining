from tkinter import *
from tkinter import messagebox
root=Tk()
def msg():
    res=messagebox.askyesnocancel("Question","Are you a Good citizen?")
    print(res)
    if res==True:
        print("Yes")
    elif res==False:
        print("no")
    else:
        print("do Nothing")
btn3=Button(root,text="Right click",
           font=("comic Sans Ms", 15, "bold"), fg="green",command=msg)
btn3.pack()
root.geometry("600x400+600+300")
root.resizable(0,0)
root.mainloop()