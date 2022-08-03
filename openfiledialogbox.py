from tkinter import *
from tkinter import filedialog

root=Tk()
def openfile():
    m=filedialog.askopenfile(initialdir="/",title="Tkinter Open file",
                           filetype=(("TEXT FILE","*.txt"),("ALL FILE","*.*")))
    #print(m)
    for i in m:
        t.insert(INSERT, i)
t=Text(root,width=20,height=10,wrap=WORD,padx=10,pady=10,selectbackground='red',
       font=("comic sans Ms",25,"bold"))
t.pack()
btn2 = Button(root, text="Open file",
                font=("comic Sans Ms", 10, "bold"), fg="green", command=openfile)
btn2.pack()
root.geometry("600x800+120+300")
#root.resizable(0,0)
root.mainloop()