from tkinter import *
root=Tk()
def getdata():
    print(t.get(2.2,END))

t=Text(root,width=20,height=10,wrap=WORD,padx=10,pady=10,selectbackground='red',
       font=("comic sans Ms",25,"bold"))
t.pack()

btn2 = Button(root, text="getdata",
                font=("comic Sans Ms", 15, "bold"), fg="green", command=getdata)
btn2.pack()
root.geometry("600x400+600+300")
#root.resizable(0,0)
root.mainloop()