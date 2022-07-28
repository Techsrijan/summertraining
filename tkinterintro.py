from tkinter import *
root=Tk()
label=Label(root,text="Enter First Number",
            font=("comic Sans Ms",15,"bold"),bg="red",fg="yellow")
label2=Label(root,text="Enter Second Number",
            font=("comic Sans Ms",15,"bold"),bg="red",fg="yellow")

label3=Label(root,text="E",
            font=("comic Sans Ms",15,"bold"),bg="red",fg="yellow")
label4=Label(root,text="Enter fourth Number",
            font=("comic Sans Ms",15,"bold"),bg="red",fg="yellow")
label.pack(side="top")
label3.pack(side="left",fill="y")
label2.pack(side="bottom")
label4.pack(side="right")
root.geometry("600x400+600+300")
root.mainloop()