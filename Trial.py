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
x1="developer"
x2="cars"
x3="bill"
mycursor.execute("""show tables where tables_in_MODCARS not like "%s" and tables_in_MODCARS not like "%s" and tables_in_MODCARS not like "%s" """%(x1,x2,x3));
for i in mycursor.fetchall():
        print(i)
