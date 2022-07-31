from tkinter import *
root=Tk()
def msg():
    print("hello")
main_menu=Menu(root)
root.config(menu=main_menu)
#filemenu
fileMenu=Menu(main_menu,tearoff=False)
main_menu.add_cascade(label="File",menu=fileMenu)

fileMenu.add_command(label="New",accelerator="Ctrl+N",command=msg)
fileMenu.add_separator()
fileMenu.add_command(label="Exit",accelerator="Ctrl+x")

#editmenu

editMenu=Menu(main_menu)
main_menu.add_cascade(label="Edit",menu=editMenu)
editMenu.add_command(label="Copy",accelerator="Ctrl+C")
root.geometry("600x400+600+300")
root.resizable(0,0)
root.mainloop()