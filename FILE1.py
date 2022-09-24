import mysql.connector
import tkinter as tk
from tkinter import *
from tkinter import messagebox as m
from tkinter import ttk

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='vijaydatabase',
    port='3306',
    database="MODCARS"
)

mycursor = mydb.cursor()




def exid():
    #wdev.destroy()
    print("")

def ndev():
    wadd_dev = tk.Tk()
    wadd_dev.geometry('600x399')
    wadd_dev.title("Add Developer")

def submitd():
    dn = vd1.get()
    dp = vd2.get()
    mycursor.execute("Select password from developer where Uname = (%s)", (dn,))
    for i in mycursor.fetchone():
        if dp == i:
            print("Valid")
        else:
            print("Not valid")

def dev():
    wdev = tk.Tk()
    wdev.geometry('600x399')
    wdev.title("Developer Validation")
    # bgdev = PhotoImage(file='developer.png')
    # imgd = tk.Label(wdev, image = bgdev)
    # imgd.place(x=0, y=0, relwidth=1, relheight=1)



    l1d = tk.Label(wdev, text="Welcome Developer", font=("Arial", 25, "bold"), fg='red')
    l1d.place(x=150, y=25)

    txtd1=tk.Entry(wdev,width=20,textvariable=vd1,font=("Arial",12))
    txtd1.place(x=200, y=150)
    l2d = tk.Label(wdev, text="Username: ", font=("Arial", 10, "bold"), fg='red')
    l2d.place(x=100, y=150)

    txtd1 = tk.Entry(wdev, width=20, textvariable=vd2, font=("Arial", 12),show='*')
    txtd1.place(x=200, y=200)
    l3d = tk.Label(wdev, text="Password: ", font=("Arial", 10, "bold"), fg='red')
    l3d.place(x=100, y=200)

    btd1 = tk.Button(wdev, text="Submit", font=("Arial", 12, "bold"), command=submitd)
    btd1.place(x=250, y=250)

    btd2 = tk.Button(wdev, text="Back", font=("Arial", 12, "bold"), command=exid)
    btd2.place(x=500, y=300)

    btd3 = tk.Button(wdev, text="New Developer? Register", font=("Arial", 12, "bold"), command=ndev)
    btd3.place(x=200, y=300)

#


def user():
    def exiu():
        wuser.destroy()


    wuser = Toplevel()
    wuser.geometry('600x399')
    wuser.title("User Options")
    icon2 = PhotoImage(file='swift (1).png')
    wuser.iconphoto(True, icon2)

    bguser = PhotoImage(file='user.png')
    imguser = tk.Label(wuser, image=bguser)
    imguser.place(x=0, y=0, relwidth=1, relheight=1)




w = tk.Tk()
w.geometry('600x363')
w.title("MODCARS")
icon = PhotoImage(file='swift (1).png')
w.iconphoto(True, icon)

bg = PhotoImage(file='bgmain.png')
img = tk.Label(w, image=bg)
img.place(x=0, y=0, relwidth=1, relheight=1)


vd1 = tk.StringVar()
vd2 = tk.StringVar()

l1 = tk.Label(w, text="MODCARS", font=("Arial", 25, "bold"), fg='red', bg='white')
# l1.grid(column=3,row=0,pady=50)
l1.place(x=210, y=25)
bt1 = tk.Button(w, text="Developer", font=("Arial", 12, "bold"), command=dev)
bt1.place(x=175, y=200)
# bt1.grid(column=2,row=3,padx=100)
bt2 = tk.Button(w, text="User", font=("Arial", 12, "bold"), command=user)
bt2.place(x=300, y=200)
# bt2.grid(column=3,row=3)

# bt2.grid(column=4,row=3,padx=20)


w.mainloop()
