from USER import *
from DEVELOPER import *

w = tk.Tk()
w.geometry('950x600+50+50')
w.configure(bg="white")
w.title("MODCARS")
icon = PhotoImage(file='swift (1).png')
w.iconphoto(True, icon)

img1 = PhotoImage(file='login.png')
img = tk.Label(w, image=img1)
img.place(x=13, y=0)

l1 = tk.Label(w, text="MODCARS", font=("Arial", 25, "bold"), fg='red', bg="white")
l1.place(x=400, y=10)
l1 = tk.Label(w, text="Welcome to MODCARS!\nLogin to continue", font=("Arial", 12, "bold"), fg='Blue', bg="white")
l1.place(x=400, y=180)
bt1 = tk.Button(w, text="Developer?", font=("Calibri", 12, "bold"),bg="white", command=dev)
bt1.place(x=820, y=20)
bt2 = tk.Button(w, text="Login", font=("Calibri", 12, "bold"), bg = "white",command=user)
bt2.place(x=620, y=240)

w.mainloop()

