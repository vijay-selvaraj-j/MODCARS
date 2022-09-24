import mysql.connector
import smtplib
import random
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


def user():
    wuser = Toplevel()
    wuser.geometry('900x500')
    wuser.title("User Options")
    car = tk.StringVar()
    pro = tk.StringVar()
    vu1 = tk.StringVar()
    vu2 = tk.StringVar()
    vu3 = tk.StringVar()
    vu12 = tk.StringVar()

    def ab():
        n = vu3.get()
        p = vu12.get()
        try:
            mycursor.execute("""Select cost from %s where name = '%s'""" % (cnui1, n,))
            for i in mycursor.fetchone():
                mycursor.execute("Insert into bill (name,cost) values (%s,%s)", (n, i))
                m.showinfo("Success", "Details Added Successfully!!!")
                mydb.commit()
        except:
            m.showerror("Error","Please Enter the Product name correctly")

    def bill():

        wubill = Toplevel()
        wubill.geometry('600x500')
        wubill.title("Bill")

        def disc():
            mycursor.execute("truncate bill")
            m.showinfo("Done!","Bill Cleared")
            wubill.destroy()

        frame = Frame(wubill)
        sql = "SELECT * FROM  bill "
        mycursor.execute(sql)
        rows = mycursor.fetchall()
        total = mycursor.rowcount

        frame.pack(side=tk.LEFT, padx=20)
        tv = ttk.Treeview(frame, columns=(1, 2), show="headings", height="10")
        tv.pack()
        tv.heading(1, text="Name")
        tv.heading(2, text="cost")
        for i in rows:
            tv.insert('', 'end', values=i)

        lub2 = tk.Label(wubill, text="TOTAL", font=("Arial", 10, "bold"), fg='red', bg="white")
        lub2.place(x=90, y=400)

        mycursor.execute("select sum(cost) from bill")
        for i in mycursor.fetchone():
            tc=i
        lub2 = tk.Label(wubill, text=tc, font=("Arial", 10, "bold"), fg='red', bg="white")
        lub2.place(x=210, y=400)

        bbtu1 = tk.Button(wubill, text="Clear Bill", command=disc)
        bbtu1.place(x=490, y=440)

        wubill.mainloop()

    def item_selected(event):
        global cn
        cn = car.get()

    def item_selectedu1(event):
        global cnui1
        cnui1 = vu12.get()

    frame = Frame(wuser)
    frame.place(x=350, y=150)
    tv = ttk.Treeview(frame, columns=(1, 2), show="headings", height="10")
    tv.pack()
    tv.heading(1, text="Name")
    tv.heading(2, text="cost")

    def sea():
        for item in tv.get_children():
            tv.delete(item)
        p = vu12.get()
        try:
            mycursor.execute("""Select name,cost from %s where model = '%s'""" % (p, cn,))
        except:
            m.showerror("Error","Product doesn't exist")


        rows = mycursor.fetchall()


        for i in rows:
            tv.insert('', 'end', values=i)

    a = []
    b = []
    mycursor.execute("truncate bill")
    mycursor.execute("Select * from cars")
    for i in mycursor.fetchall():
        a.append(i)

    cb1 = ttk.Combobox(wuser, width=27, textvariable=car)
    cb1.place(x=330, y=50)
    cb1['values'] = (a)
    cb1['state'] = 'readonly'
    cb1.bind('<<ComboboxSelected>>', item_selected)

    """cb2 = ttk.Combobox(wuser, width=27, textvariable=pro)
    cb2.place(x=100, y=300)
    cb2['values'] = (b)
    cb2['state'] = 'readonly'
    cb2.bind('<<ComboboxSelected>>', item_selected1)"""

    lu1 = tk.Label(wuser, text="Select Car ", font=("Arial", 10, "bold"), fg='red', bg="white")
    lu1.place(x=180, y=50)

    lu2 = tk.Label(wuser, text="Select Part ", font=("Arial", 10, "bold"), fg='red', bg="white")
    lu2.place(x=180, y=100)


    btu1 = tk.Button(wuser, text="Search", command=sea)
    btu1.place(x=150, y=180)

    tu2 = tk.Entry(wuser, width=27, textvariable=vu3)
    tu2.place(x=330, y=400)
    btu2 = tk.Button(wuser, text="Add Into Bill", command=ab)
    btu2.place(x=150, y=400)

    btu3 = tk.Button(wuser, text="Show Bill", command=bill)
    btu3.place(x=150, y=440)

    uci2 = []
    x1 = "developer"
    x2 = "cars"
    x3 = "bill"
    mycursor.execute("""show tables where tables_in_MODCARS not like "%s" and tables_in_MODCARS not like "%s" and tables_in_MODCARS not like "%s" """ %(x1, x2, x3,));

    for i in mycursor.fetchall():
        uci2.append(i)

    cbu2 = ttk.Combobox(wuser, width=27, textvariable=vu12)
    cbu2.place(x=330, y=100)
    cbu2['values'] = (uci2)
    cbu2['state'] = 'readonly'
    cbu2.bind('<<ComboboxSelected>>', item_selectedu1)