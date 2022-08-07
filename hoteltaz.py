from tkinter import *
from tkinter import messagebox
import pymysql
from PIL import Image,ImageTk


taz=Tk()

user_icon=ImageTk.PhotoImage(Image.open('images/user.png'))

def only_char_input(P):
    # checks if entry's value is an character  and returns an appropriate boolean
    if P.isalpha() or P == "":
    #if P.isalpha() or P == :  # if a digit was entered or nothing was entered
        return True
    return False
callback = taz.register(only_char_input)  # registers a Tcl to Python callb
#########################remove all widgets from screen #################

def remove_all_widgets():
    global taz
    for widget in taz.winfo_children():
        widget.grid_remove()
########### Welcome Window ################
def welcomewindow():
    remove_all_widgets()
    mainheading()
    additemwindow()

#### database Connection ################
def db_connect():
    global mycursor, connection
    connection = pymysql.connect(user="root", host="127.0.0.1", db="summer")
    mycursor = connection.cursor()

############mainheading##############
def mainheading():
    label=Label(taz,text="Hotel Management System",bg="yellow",fg="red",
                font=("Comic Sans Ms","48","bold"),padx=100)
    label.grid(row=0,columnspan=5)

usernameVar = StringVar()
passwordVar = StringVar()
############### admin login ############
def adminlogin():
    username = usernameVar.get()
    password = passwordVar.get()
    if username=='' or password=='':
        messagebox.showerror("Login Error","Please enter Both Fields")
    else:
        db_connect()
        que = "select * from login_info where binary username=%s and binary password=%s"
        val = (username,password)
        mycursor.execute(que,val)
        data = mycursor.fetchall()
        flag = False
        for row in data:
            flag = True

        connection.close()
        if flag == True:
            welcomewindow()

        else:
            messagebox.showerror("Invalid User Credential", 'either User Name or Password is incorrect')
            usernameVar.set("")
            passwordVar.set("")

############ login window ##############

def login_window():

    loginLabel = Label(taz, text="Admin Login",image=user_icon,compound=LEFT,font="Arial 30")
    loginLabel.grid(row=1, column=1, padx=(50, 0), columnspan=2, pady=10)

    usernameLabel = Label(taz, text="Username")
    usernameLabel.grid(row=2, column=1, padx=20, pady=5)

    passwordLabel = Label(taz, text="Password")
    passwordLabel.grid(row=3, column=1, padx=20, pady=5)

    usernameEntry = Entry(taz, textvariable=usernameVar)
    usernameEntry.grid(row=2, column=2, padx=20, pady=5)
    #usernameEntry.configure(validate="key", validatecommand=(callback, "%P"))

    passwordEntry = Entry(taz, show="*", textvariable=passwordVar)
    passwordEntry.grid(row=3, column=2, padx=20, pady=5)

    loginButton = Button(taz, text="Login", width=20, height=2, fg="green", bd=10, command=adminlogin)
    loginButton.grid(row=4, column=1, columnspan=2)


def additem():
    name = itemnameVar.get()
    rate = itemrateVar.get()
    type = itemTypeVar.get()
    print(name, rate, type)
    db_connect()
    query = "insert into itemlist (item_name,item_rate,item_type) values(%s,%s,%s);"
    val = (name, rate, type)
    mycursor.execute(query, val)
    connection.commit()
    messagebox.showinfo("Save Data", 'Item Inserted Successfully')
    itemnameVar.set("")
    itemrateVar.set("")
    itemTypeVar.set("")

################## add item window ##################
itemnameVar=StringVar()
itemrateVar=StringVar()
itemTypeVar=StringVar()

def additemwindow():
    remove_all_widgets()
    mainheading()

    itemnameLabel = Label(taz, text="ITEM DETAILS", font="Arial 30")
    itemnameLabel.grid(row=1, column=2, padx=(50, 0), columnspan=1, pady=10)

    ###############################
    '''
    billButton = Button(taz, text="Back", width=20, height=2, fg="green", bd=10, command=backbutton)
    billButton.grid(row=1, column=0, columnspan=1)

    logoutButton = Button(taz, text="Logout", width=20, height=2, fg="green", bd=10, command=logout)
    logoutButton.grid(row=3, column=0, columnspan=1)
    '''
    ###########################

    itemnameLabel = Label(taz, text="Item name")
    itemnameLabel.grid(row=2, column=1, padx=20,  pady=5)


    itemrateLabel = Label(taz, text="Item Rate")
    itemrateLabel.grid(row=3, column=1, padx=20, pady=5)

    itemTypeLabel = Label(taz, text="Item Type")
    itemTypeLabel.grid(row=4, column=1, padx=20, pady=5)

    itemnameEntry = Entry(taz, textvariable=itemnameVar)
    itemnameEntry.grid(row=2, column=2, padx=20, pady=5)
    itemnameEntry.configure(validate="key", validatecommand=(callback, "%P"))  # enables validation

    itemrateEntry = Entry(taz, textvariable=itemrateVar)
    itemrateEntry.grid(row=3, column=2, padx=20, pady=5)
    #itemrateEntry.configure(validate="key", validatecommand=(callback1, "%P"))  # enables validation

    itemTypeEntry = Entry(taz, textvariable=itemTypeVar)
    itemTypeEntry.grid(row=4, column=2, padx=20, pady=5)
    #itemTypeEntry.configure(validate="key", validatecommand=(callback, "%P"))  # enables validation


    label = Label(taz)
    label.grid(row=5, column=2, padx=20, pady=5)

    additemButton = Button(taz, text="Add Item", width=20, height=2, fg="green", bd=10,command=additem)
    additemButton.grid(row=3, column=3, columnspan=1)
    '''
    updateButton = Button(taz, text="UpDate Item", width=20, height=2, fg="green", bd=10, command=updateItem)
    updateButton.grid(row=1, column=3, columnspan=1)

    deleteButton = Button(taz, text="Delete Item", width=20, height=2, fg="green", bd=10,command=deleteItem)
    deleteButton.grid(row=6, column=3, columnspan=1)

    ###############################################
    tazTV.grid(row=7, column=0, columnspan=3)
    style=ttk.Style(taz)
    style.theme_use('clam')
    style.configure("Treeview",fieldbackground="green")
    scrollBar = Scrollbar(taz, orient="vertical", command=tazTV.yview)
    scrollBar.grid(row=7, column=2, sticky="NSE")

    tazTV.configure(yscrollcommand=scrollBar.set)

    tazTV.heading('#0', text="Item Name")
    tazTV.heading('#1', text="Rate")
    tazTV.heading('#2', text="Type")

    getItemInTreeView()
    '''
taz.title("Hotel Management System")
mainheading()
login_window()
h=taz.winfo_screenheight()
w=taz.winfo_screenwidth()
print()
taz.geometry("%dx%d+0+0"%(w,h))
taz.mainloop()