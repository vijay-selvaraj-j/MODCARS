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


def dev():

    wdev = Toplevel()
    wdev.geometry('470x450')
    wdev.title("Developer Validation")
    img2 = PhotoImage(file='developer.png')
    img3 = tk.Label(wdev, image=img2)
    img3.pack()
    #********************************************************************************************************************

    def exid():
        wdev.destroy()

#*******************************************************************************************************************

    def idevotp():
        na = vd3.get()
        pc2 = vd5.get()
        ot = vd7.get()
        if ot == otp:
            mycursor.execute("Insert into developer (UName,password) values (%s,%s)", (na, pc2))
            m.showinfo("Success", "Details Added Successfully!!!")
            mydb.commit()
        else:
            m.showerror("Denied","Invalid OTP")

#******************************************************************************************************************

    def idev():
        na1=vd3.get()
        pa=vd4.get()
        pc1=vd5.get()
        em=vd6.get()
        sender="modcarssolutions@gmail.com"
        receiver="1nh19cs198.Vijay@gmail.com"
        password='yumqkcxzjqnavglt'
        subject="MODCARS Authentication"
        body="New Developer " +na1+ " : " +em+ " is trying to login as administer. \n The One-Time-Password for your MODCARS admin registration is "+str(otp)
        msg = f"""From: MODCARS{sender}
        To: New Developer{receiver}
        Subject: {subject}\n
        {body}
        """
        if pa == pc1:
            server=smtplib.SMTP('smtp.gmail.com',587)
            server.starttls()
            try:
                server.login('modcarssolutions@gmail.com',password)
                server.sendmail(sender,receiver,msg)
                server.quit()
            except smtplib.SMTPAuthenticationError:
                print("Unable to send Email")

        else:
            m.showerror("Error","Passwords don't match")

#*******************************************************************************************************************

    def ndev():
        wadd_dev = Toplevel()
        wadd_dev.geometry('450x450')
        wadd_dev.title("Add Developer")

        lnd0 = tk.Label(wadd_dev, text="Enter Details", font=("Arial", 14, "bold"), fg='red')
        lnd0.place(x=170, y=30)

        txtnd1 = tk.Entry(wadd_dev, width=20, textvariable=vd3, font=("Arial", 12))
        txtnd1.place(x=200, y=100)
        lnd1 = tk.Label(wadd_dev, text="Enter Username: ", font=("Arial", 10, "bold"), fg='blue')
        lnd1.place(x=50, y=100)

        txtnd2 = tk.Entry(wadd_dev, width=20, textvariable=vd4, font=("Arial", 12), show='*')
        txtnd2.place(x=200, y=150)
        lnd2 = tk.Label(wadd_dev, text="Enter Password: ", font=("Arial", 10, "bold"), fg='blue')
        lnd2.place(x=50, y=150)

        txtnd3 = tk.Entry(wadd_dev, width=20, textvariable=vd5, font=("Arial", 12), show='*')
        txtnd3.place(x=200, y=200)
        lnd3 = tk.Label(wadd_dev, text="Confirm Password: ", font=("Arial", 10, "bold"), fg='blue')
        lnd3.place(x=50, y=200)

        txtnd3 = tk.Entry(wadd_dev, width=20, textvariable=vd6, font=("Arial", 12))
        txtnd3.place(x=200, y=250)
        lnd3 = tk.Label(wadd_dev, text="Email ID: ", font=("Arial", 10, "bold"), fg='blue')
        lnd3.place(x=50, y=250)

        btnd1 = tk.Button(wadd_dev, text="Generate OTP", font=("Arial", 12, "bold"), command=idev)
        btnd1.place(x=200, y=300)

        txtnd4 = tk.Entry(wadd_dev, width=20, textvariable=vd7, font=("Arial", 12))
        txtnd4.place(x=200, y=350)
        lnd4 = tk.Label(wadd_dev, text="Enter OTP: ", font=("Arial", 10, "bold"), fg='blue')
        lnd4.place(x=50, y=350)

        btnd2 = tk.Button(wadd_dev, text="Submit", font=("Arial", 12, "bold"), command=idevotp)
        btnd2.place(x=200, y=385)

#*********************************************************************************************************************************

    def rdev():

        def rdevsu():
            mycursor.execute("Select password from developer where Uname = 'Vijay'")
            for i in mycursor.fetchone():
                passw=i

            a = vd16.get()
            b = vd18.get()
            if b==passw:
                mycursor.execute("delete from developer where UName = (%s)", (a,))
                m.showinfo("Success", "Developer Removed Successfully!!!")
                mydb.commit()
                #for i in mycursor.fetchone():
            else:
                m.showerror("Restricted","Incorrect Password")

        rdev=Toplevel()
        rdev.geometry('450x500')
        try:
            l1=[]
            mycursor.execute('Select UName from developer where not UName = "Vijay"')
            na=mycursor.fetchall()
            for i in na:
                l1.append(i[0])
            op=tk.OptionMenu(rdev,vd16,*l1)
            op.place(x=200,y=120)

            lr1 = tk.Label(rdev, text="Select Name: ", font=("Arial", 10, "bold"), fg='blue')
            lr1.place(x=50, y=120)
            lr2 = tk.Label(rdev, text="Enter Password: ", font=("Arial", 10, "bold"), fg='blue')
            lr2.place(x=50, y=170)
            tr2 = tk.Entry(rdev, width=20, textvariable=vd18, font=("Arial", 12),show='*')
            tr2.place(x=200, y=170)
            br=tk.Button(rdev,text="Remove", font=("Arial", 10, "bold"), bg="white",command=rdevsu)
            br.place(x=100,y=220)
        except:
            m.showerror("ERROR","No Developers found")

    def submitd():
        dn = vd1.get()
        dp = vd2.get()

# *******************************************************************************************************************
        def devadd():

            def addcar():
                try:
                    cname1=vd8.get()
                    mycursor.execute("Insert into cars values (%s)", (cname1,))
                    m.showinfo("Success", "Model Added Successfully!!!")
                    mydb.commit()
                    ddadd.destroy()
                except:
                    m.showerror("ERROR","Car Already Exists")


            ddadd=Toplevel()
            ddadd.geometry('800x500')
            ddadd.title("Add Products")
            tdaddc = tk.Entry(ddadd, width=20, textvariable=vd8, font=("Arial", 12))
            tdaddc.place(x=160, y=100)
            ldadd = tk.Label(ddadd, text="Car Model: ", font=("Arial", 12, "bold"), fg='blue', bg="white")
            ldadd.place(x=35, y=100)
            bdadd = tk.Button(ddadd, text="Add", font=("Arial", 10, "bold"), bg="white", command=addcar)
            bdadd.place(x=135, y=150)


# *******************************************************************************************************************

        def devup():

            def item_selecteddu(event):
                global cndu
                cndu = cardu.get()


            def upcar():
                cname3 = vd10.get()
                cname4 = vd11.get()
                mycursor.execute("update cars set name = (%s) where name = (%s)", (cname4,cndu))
                m.showinfo("Success", "Model Updated Successfully!!!")
                mydb.commit()
                ddup.destroy()

            ddup = Toplevel()
            ddup.geometry('800x500')
            ddup.title("Update Products")


            ldup1 = tk.Label(ddup, text="Car Model: ", font=("Arial", 12, "bold"), fg='blue', bg="white")
            ldup1.place(x=35, y=100)
            tdup2 = tk.Entry(ddup, width=20, textvariable=vd11, font=("Arial", 12))
            tdup2.place(x=180, y=150)
            ldup2 = tk.Label(ddup, text="New Name: ", font=("Arial", 12, "bold"), fg='blue', bg="white")
            ldup2.place(x=35, y=150)
            bdup = tk.Button(ddup, text="Update", font=("Arial", 10, "bold"), bg="white", command=upcar)
            bdup.place(x=125, y=200)

            dcu = []
            mycursor.execute("Select * from cars")
            for i in mycursor.fetchall():
                dcu.append(i)

            cbdu1 = ttk.Combobox(ddup, width=27, textvariable=cardu)
            cbdu1.place(x=180, y=100)
            cbdu1['values'] = (dcu)
            cbdu1['state'] = 'readonly'
            cbdu1.bind('<<ComboboxSelected>>', item_selecteddu)

# *******************************************************************************************************************

        def devdel():

            def item_selectedd(event):
                global cnd
                cnd = card.get()

            def delcar():


                try:
                    cname2=vd9.get()
                    mycursor.execute("delete from cars where name = (%s)", (cnd,))
                    m.showinfo("Success", "Model Deleted Successfully!!!")
                    mydb.commit()
                    dddel.destroy()
                except:
                    m.showerror("Error","Model Doesn't Exists")
            dddel = Toplevel()
            dddel.geometry('800x500')
            dddel.title("Delete Products")

            lddel = tk.Label(dddel, text="Car Model: ", font=("Arial", 12, "bold"), fg='blue', bg="white")
            lddel.place(x=35, y=100)
            bddel = tk.Button(dddel, text="Delete", font=("Arial", 10, "bold"), bg="white", command=delcar)
            bddel.place(x=155, y=150)

            dc = []
            mycursor.execute("Select * from cars")
            for i in mycursor.fetchall():
                dc.append(i)

            cbd1 = ttk.Combobox(dddel, width=27, textvariable=card)
            cbd1.place(x=160, y=100)
            cbd1['values'] = (dc)
            cbd1['state'] = 'readonly'
            cbd1.bind('<<ComboboxSelected>>', item_selectedd)

# *******************************************************************************************************************

        try:
            def item_selecteddi(event):
                global cndi
                cndi = vd14.get()

            def item_selecteddi2(event):
                global cndi2
                cndi2 = vd12.get()


            mycursor.execute("Select password from developer where Uname = (%s)", (dn,))
            for i in mycursor.fetchone():

                if dp == i:

                    wdch=Toplevel()
                    ldic1 = tk.Label(wdch, text="CAR MODEL ", font=("Arial", 12, "bold"), fg='red', bg="white")
                    ldic1.place(x=390, y=30)
                    wdch.geometry('800x500+50+50')
                    b1 = tk.Button(wdch, text="Insert Car", font=("Arial", 10, "bold"), bg="white",command=devadd)
                    b1.place(x=290, y=80)
                    b2 = tk.Button(wdch, text="Update Car", font=("Arial", 10, "bold"), bg="white",command=devup)
                    b2.place(x=390, y=80)
                    b3 = tk.Button(wdch, text="Delete Car", font=("Arial", 10, "bold"), bg="white",command=devdel)
                    b3.place(x=490, y=80)

                    ldic2 = tk.Label(wdch, text="PRODUCTS ", font=("Arial", 12, "bold"), fg='red', bg="white")
                    ldic2.place(x=390, y=180)

                    def ip():
                        pt = vd12.get()
                        pn = vd13.get()
                       # mn = vd14.get()
                        pc=int(vd15.get())
                        try:
                            mycursor.execute("""insert into %s values ('%s','%s',%s)"""%(cndi2,pn,cndi,pc,))
                            m.showinfo("Success", "Product Inserted Successfully!")
                            mydb.commit()
                        except:
                            m.showerror("Error","Product doesn't exist")

                    def ad():
                        pt=vd17.get()
                        try:
                            mycursor.execute("""create table %s (name varchar(40) primary key, model varchar(40) not null,cost int not null, foreign key(model) references cars(name))"""%pt,)
                            m.showinfo("Success","Product Created Successfully!")
                            mydb.commit()
                        except:
                            m.showerror("Error","Invalid Format")
                    def de():
                        pt = vd17.get()
                        mycursor.execute("""drop table %s """ %pt,)
                        m.showinfo("Success", "Product Deleted Successfully!")
                        mydb.commit()


                    ldic3 = tk.Label(wdch, text="Product Type: ", font=("Arial", 12, "bold"), fg='blue', bg="white")
                    ldic3.place(x=50, y=250)
                    tdic1 = tk.Entry(wdch, width=20, textvariable=vd12, font=("Arial", 12))
                    tdic1.place(x=200, y=250)
                    ldic3 = tk.Label(wdch, text="Product Name: ", font=("Arial", 12, "bold"), fg='blue', bg="white")
                    ldic3.place(x=50, y=300)
                    tdic1 = tk.Entry(wdch, width=20, textvariable=vd13, font=("Arial", 12))
                    tdic1.place(x=200, y=300)
                    ldic4 = tk.Label(wdch, text="Model Name: ", font=("Arial", 12, "bold"), fg='blue', bg="white")
                    ldic4.place(x=50, y=350)

                    ldic5 = tk.Label(wdch, text="Product Cost: ", font=("Arial", 12, "bold"), fg='blue', bg="white")
                    ldic5.place(x=50, y=400)
                    tdic3 = tk.Entry(wdch, width=20, textvariable=vd15, font=("Arial", 12))
                    tdic3.place(x=200, y=400)


                    dci = []
                    mycursor.execute("Select * from cars")
                    for i in mycursor.fetchall():
                        dci.append(i)

                    cbd1 = ttk.Combobox(wdch, width=27, textvariable=vd14)
                    cbd1.place(x=200, y=350)
                    cbd1['values'] = (dci)
                    cbd1['state'] = 'readonly'
                    cbd1.bind('<<ComboboxSelected>>', item_selecteddi)

                    dci2 = []
                    x1 = "developer"
                    x2 = "cars"
                    x3 = "bill"
                    mycursor.execute("""show tables where tables_in_MODCARS not like "%s" and tables_in_MODCARS not like "%s" and tables_in_MODCARS not like "%s" """%(x1,x2,x3));

                    for i in mycursor.fetchall():
                        dci2.append(i)

                    cbd2 = ttk.Combobox(wdch, width=27, textvariable=vd12)
                    cbd2.place(x=200, y=250)
                    cbd2['values'] = (dci2)
                    cbd2['state'] = 'readonly'
                    cbd2.bind('<<ComboboxSelected>>', item_selecteddi2)

                    ldic6 = tk.Label(wdch, text="Add/Delete Product: ", font=("Arial", 12, "bold"), fg='blue', bg="white")
                    ldic6.place(x=50, y=450)
                    tdic6 = tk.Entry(wdch, width=20, textvariable=vd17, font=("Arial", 12))
                    tdic6.place(x=250, y=450)

                    b4 = tk.Button(wdch, text="Insert", font=("Arial", 10, "bold"), bg="white", command=ip)
                    b4.place(x=490, y=280)
                    b5 = tk.Button(wdch, text="Add", font=("Arial", 10, "bold"), bg="white", command=ad)
                    b5.place(x=490, y=330)
                    b6 = tk.Button(wdch, text="Delete", font=("Arial", 10, "bold"), bg="white", command=de)
                    b6.place(x=490, y=380)

                else:
                    m.showerror("ERROR", "Invalid Credentials")
                    wdev.destroy()
        except:
            m.showerror("Restricted","Username not found")
            wdev.destroy()

#*******************************************************************************************************************

    wdev.configure(bg="white")

    vd1 = tk.StringVar()
    vd2 = tk.StringVar()
    vd3 = tk.StringVar()
    vd4 = tk.StringVar()
    vd5 = tk.StringVar()
    vd6 = tk.StringVar()
    vd7 = tk.StringVar()
    vd8 = tk.StringVar()
    vd9 = tk.StringVar()
    vd10 = tk.StringVar()
    vd11 = tk.StringVar()
    vd12 = tk.StringVar()
    vd13 = tk.StringVar()
    vd14 = tk.StringVar()
    vd15 = tk.StringVar()
    vd16 = tk.StringVar()
    vd17 = tk.StringVar()
    vd18 = tk.StringVar()
    card = tk.StringVar()
    cardu = tk.StringVar()

    otp = ''.join([str(random.randint(0, 9)) for i in range(6)])

    txtd1=tk.Entry(wdev,width=20,textvariable=vd1,font=("Arial",12))
    txtd1.place(x=155, y=100)
    l2d = tk.Label(wdev, text="Username: ", font=("Arial", 12, "bold"), fg='blue',bg="white")
    l2d.place(x=35, y=100)

    txtd1 = tk.Entry(wdev, width=20, textvariable=vd2, font=("Arial", 12),show='*')
    txtd1.place(x=155, y=165)
    l3d = tk.Label(wdev, text="Password: ", font=("Arial", 12, "bold"), fg='blue', bg="white")
    l3d.place(x=35, y=165)

    l4d = tk.Label(wdev, text="Login ", font=("Algerian", 18, "bold"), fg='red', bg="white")
    l4d.place(x=180, y=20)

    btd1 = tk.Button(wdev, text="Login", font=("Arial", 10, "bold"), bg="white" ,command=submitd)
    btd1.place(x=180, y=220)

    btd2 = tk.Button(wdev, text="Back", font=("Arial", 10, "bold"), bg="white" ,command=exid)
    btd2.place(x=330, y=400)

    btd3 = tk.Button(wdev, text="New Developer? Register", font=("Arial", 10, "bold"), bg="white", command=ndev)
    btd3.place(x=125, y=270)

    btd4 = tk.Button(wdev, text="Remove Developer", font=("Arial", 10, "bold"), bg="white", command=rdev)
    btd4.place(x=240, y=360)

#******************************************************************************************************************
#*****************************************************************************************************************