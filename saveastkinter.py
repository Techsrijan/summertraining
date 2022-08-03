from tkinter import *
from tkinter import filedialog

root=Tk()
f=None
def openfile():
    global f
    f=filedialog.askopenfile(initialdir="/",title="Tkinter Open file",
                           filetype=(("TEXT FILE","*.txt"),("ALL FILE","*.*")))
    print(f.name)
    for i in f:
        t.insert(INSERT, i)

def saveasfile():
    f=filedialog.asksaveasfile(mode="w",defaultextension="*.txt")
    print(f)
    if f is None:
        return
    text2save=t.get(1.0,END)
    f.write(text2save)
    f.close()

def savefile():
    print(f.name)
    if f.name==None:
        saveasfile()
    else:
        x=open(f.name,"w")
        text2save = t.get(1.0, END)
        x.write(text2save)


t=Text(root,width=20,height=10,wrap=WORD,padx=10,pady=10,selectbackground='red',
       font=("comic sans Ms",25,"bold"))
t.pack()
btn2 = Button(root, text="Open file",
                font=("comic Sans Ms", 10, "bold"), fg="green", command=openfile)
btn2.pack()

btn3 = Button(root, text="Save As",
                font=("comic Sans Ms", 10, "bold"), fg="green", command=saveasfile)
btn3.pack()


btn4 = Button(root, text="Save",
                font=("comic Sans Ms", 10, "bold"), fg="green", command=savefile)
btn4.pack()
root.geometry("600x800+120+300")
#root.resizable(0,0)
root.mainloop()