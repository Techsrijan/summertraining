from tkinter import *
root=Tk()

def msg(event):
    print("left button clicked")
def msg2(event):
    print("Middle Button Clicked")
def msg3(event):
    print("Right Button Clicked")

root.bind("<Button-1>",msg)
root.bind("<Button-2>",msg2)
root.bind("<Button-3>",msg3)
root.title("My Project")
btn=Button(root,text="Left click",
           font=("comic Sans Ms", 15, "bold"), fg="green")
btn.pack()
btn2=Button(root,text="Middle click",
           font=("comic Sans Ms", 15, "bold"), fg="green")
btn2.pack()

btn3=Button(root,text="Right click",
           font=("comic Sans Ms", 15, "bold"), fg="green")
btn3.pack()
root.wm_iconbitmap("calc.ico")
root.geometry("600x400+600+300")
root.resizable(0,0)
root.mainloop()