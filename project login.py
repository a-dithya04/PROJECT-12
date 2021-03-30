from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
from tkcalendar import DateEntry
from datetime import date 
import sqlite3

def showpass(): 
    if var.get():
        passentry.config(show="")
    else:
        passentry.config(show="•")

def exit():
    root.destroy()

root = Tk()
root.title("Lacaula Island")
#root.iconbitmap("nature.ico")
W, H=root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (W, H))

canvas = Canvas(root)
canvas.pack(fill=BOTH, expand=True)

canvas.create_rectangle(500,275,1050,710)

canvas.create_text(770,210,text="Lacaula Island",font=("Monotype Corsiva",50)) 
canvas.create_text(770,310,text="LOGIN",font=("Architects Daughter",30))

canvas.create_text(600,360,text="Username:",font=("Bahnschrift",17))
canvas.create_text(600,390,text="Password:",font=("Bahnschrift",17))


userentry=Entry(root,bd=0,width=30,font=("Calibri",12))
canvas.create_window(780,360,window=userentry)

passentry=Entry(root,bd=0,width=30,font=("Calibri",12),show="•")
canvas.create_window(780,390,window=passentry)

var=IntVar()
showbutton=Checkbutton(root,text="Show Password",font=('Playfair Display',11),borderwidth=0,variable=var,cursor="hand2",command=showpass)
canvas.create_window(980,390,window=showbutton)

image1 = ImageTk.PhotoImage(Image.open("login.png"))
login=Button(root,image=image1,borderwidth=0,cursor="hand2")
canvas.create_window(760,540,window=login)

exitbutton=Button(root,text="EXIT",borderwidth=0,cursor="hand2",command=exit)
canvas.create_window(768,600,window=exitbutton)


root.mainloop()