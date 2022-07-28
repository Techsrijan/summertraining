from tkinter import *
root=Tk()

def msg():
    print("hello")
    a=s.get()
    b=t.get()
    c=a+b
    print(c)

label=Label(root,text="Enter First Number",
            font=("comic Sans Ms",15,"bold"),bg="red",fg="yellow")

label.place(x=100,y=100)

s=IntVar()
text=Entry(root,font=("comic Sans Ms",15,"bold"),textvariable=s)
text.place(x=400,y=100)

label2=Label(root,text="Enter Second Number",
            font=("comic Sans Ms",15,"bold"),bg="red",fg="yellow")

label2.place(x=100,y=200)
t=IntVar()

text2=Entry(root,font=("comic Sans Ms",15,"bold"),textvariable=t)
text2.place(x=400,y=200)
btn=Button(root,text="Click",
           font=("comic Sans Ms", 15, "bold"), fg="green",command=msg)
btn.place(x=250,y=300)
root.geometry("600x400+600+300")
root.mainloop()