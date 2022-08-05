from tkinter import *
from tkinter import messagebox
import pymysql


taz=Tk()


#########################remove all widgets from screen #################

def remove_all_widgets():
    global taz
    for widget in taz.winfo_children():
        widget.grid_remove()
########### Welcome Window ################
def welcomewindow():
    remove_all_widgets()
    mainheading()

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
        que = "select * from login_info where username=%s and password=%s"
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

    loginLabel = Label(taz, text="Admin Login", font="Arial 30")
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

taz.title("Hotel Management System")
mainheading()
login_window()
h=taz.winfo_screenheight()
w=taz.winfo_screenwidth()
print()
taz.geometry("%dx%d+0+0"%(w,h))
taz.mainloop()