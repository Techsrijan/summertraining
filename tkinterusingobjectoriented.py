from tkinter import *

class MyWindow:
    def msg(self):
        print("hello")

    def __init__(self,win):
        self.btn=Button(win,text="Click Me",command=self.msg)
        self.btn.pack()




root=Tk()

s=MyWindow(root)
root.mainloop()


