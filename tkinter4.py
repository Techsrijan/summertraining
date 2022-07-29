from tkinter import *
root=Tk()

def msg(event=""):
    print("left button clicked")

root.bind("<Control-C>",msg)

root.title("My Project")
btn=Button(root,text="Left click",
           font=("comic Sans Ms", 15, "bold"), fg="green",command=msg)
btn.pack()
btn2=Button(root,text="CLOSE",
           font=("comic Sans Ms", 15, "bold"), fg="red",command=quit)
btn2.pack()

t=IntVar()

text2=Entry(root,font=("comic Sans Ms",15,"bold"),bd="15",bg="blue",fg="white",show="*",textvariable=t,justify="right").pack()
root.wm_iconbitmap("calc.ico")
root.geometry("600x400+600+300")
root.resizable(0,0)
root.mainloop()