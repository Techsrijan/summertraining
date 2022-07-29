from tkinter import *
root=Tk()

def msg():
    #print("hello")
    a=s.get()
    b=t.get()
    c=a+b
    #print(c)
    p.set(c)

label=Label(root,text="Enter First Number",
            font=("comic Sans Ms",15,"bold"),fg="yellow")

label.grid(row=0,column=0)

s=IntVar()
text=Entry(root,font=("comic Sans Ms",15,"bold"),textvariable=s)
text.grid(row=0,column=1)

label2=Label(root,text="Enter Second Number",
            font=("comic Sans Ms",15,"bold"),fg="yellow")

label2.grid(row=1,column=0)
t=IntVar()

text2=Entry(root,font=("comic Sans Ms",15,"bold"),textvariable=t)
text2.grid(row=1,column=1)
btn=Button(root,text="Click",
           font=("comic Sans Ms", 15, "bold"), fg="green",command=msg)
btn.grid(row=2,column=0,columnspan=2)
p=StringVar()
label3=Label(root,
            font=("comic Sans Ms",15,"bold"),fg="red",textvariable=p)

label3.grid(row=3,column=0)

res=Entry(root,
            font=("comic Sans Ms",15,"bold"),fg="red",textvariable=p)

res.grid(row=3,column=1)
#root.geometry("600x400+600+300")
root.mainloop()