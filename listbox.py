from tkinter import *
root=Tk()
def getdata():
   selected_item=l.curselection()
   print(selected_item)
   for i in selected_item:
       print(l.get(i))
def Deletedata():
    selected_item = l.curselection()
    print(selected_item)
    for i in selected_item:
        print(l.delete(i))
f=Frame(root)
scroll=Scrollbar(f)

l=Listbox(f,width=30,yscrollcommand=scroll.set,selectmode=EXTENDED)
'''
l.insert(1,"C+++++++++++++++++++++++++++hhh")
l.insert(2,"Python")'''
for i in range(1,32):
    l.insert(i,i)
l.pack(side=LEFT)

scroll.config(command=l.yview)
scroll.pack(side=RIGHT,fill=Y)

f.pack()

btn2 = Button(root, text="getdata",
                font=("comic Sans Ms", 10, "bold"), fg="green", command=getdata)
btn2.pack()

btn3 = Button(root, text="Deletedata",
                font=("comic Sans Ms", 10, "bold"), fg="red", command=Deletedata)
btn3.pack()
root.geometry("600x800+120+300")
root.mainloop()