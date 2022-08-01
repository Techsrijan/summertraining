from tkinter import *
root=Tk()
def getdata():
    print(t.get(1.0,END))
def sel_getdata():
    res=t.selection_get()
    print(res)
def clear():
    t.delete(1.0,END)
def select_pos():
    res = t.selection_get()
    pos=t.search(res,1.0,stopindex=END)
    print(pos)
t=Text(root,width=20,height=10,wrap=WORD,padx=10,pady=10,selectbackground='red',
       font=("comic sans Ms",25,"bold"))
t.pack()

f=open("test.txt","r")
for i in f:
    t.insert(INSERT, i)
    
t.insert(INSERT,"This is class")


btn2 = Button(root, text="getdata",
                font=("comic Sans Ms", 10, "bold"), fg="green", command=getdata)
btn2.pack()

btn3 = Button(root, text="get selected data",
                font=("comic Sans Ms", 10, "bold"), fg="blue", command=sel_getdata)
btn3.pack()
btn4 = Button(root, text="clear ",
                font=("comic Sans Ms", 10, "bold"), fg="red", command=clear)
btn4.pack()

btn5 = Button(root, text="get position ",
                font=("comic Sans Ms", 10, "bold"), fg="red", command=select_pos)
btn5.pack()
root.geometry("600x800+120+300")
#root.resizable(0,0)
root.mainloop()