from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
from tkcalendar import DateEntry
from datetime import date 
import sqlite3

# func to display password in login screen
def showpass(): 
    if var.get():
        passentry.config(show="")
    else:
        passentry.config(show="•")

#func for exit button in login screen
def exit():
    root.destroy()

#func for loading splash screen
x= 1               
def update():
    global x, id
    if x==6:
        canvas.delete("o")
        canvas.delete("t")
        canvas.delete("th")
        canvas.delete("f")
        canvas.delete("fi")
        x=1

    if x==1:
        load.config(text = "Loading.")
        canvas.create_window(200,340,window=circle1,tag="o")

    elif x==2:
        load.config(text = "Loading..")
        canvas.create_window(250,340,window=circle2,tag="t")

    elif x==3:
        load.config(text = "Loading...")     
        canvas.create_window(300,340,window=circle3,tag="th")

    elif x==4:
        load.config(text = "Loading....")     
        canvas.create_window(350,340,window=circle4,tag="f")

    elif x==5:
        load.config(text = "Loading.....")     
        canvas.create_window(400,340,window=circle5,tag="fi")

    x +=1
    id=root.after(500,update)

# after loading screen is over, this func is called and new screen is displayed
def come():
    global image1,image2,image3, passentry, var
    #size of screen is changed and old widgets in canvas are deleted
    root.geometry("%dx%d+0+0" % (W, H))
    root.after_cancel(id)
    canvas.delete("all")
    

    image1 = ImageTk.PhotoImage(Image.open("log2.jpg"))
    canvas.create_image(W/2,450,image=image1)

    image2 = ImageTk.PhotoImage(Image.open("bglogo.png"))
    canvas.create_image(W/2,100,image=image2)

    canvas.create_rectangle(500,275,1050,710,fill="white",outline="skyblue",width=5)

    canvas.create_text(770,210,text="Lacaula Island",fill = "white",font=("Monotype Corsiva",50)) 
    canvas.create_text(770,330,text="LOGIN",font=("Architects Daughter",30))

    canvas.create_text(590,400,text="Username:",font=("Bahnschrift",19))
    canvas.create_text(590,445,text="Password:",font=("Bahnschrift",19))


    userentry=Entry(root,bd=5,width=30,relief = "ridge",font=("Calibri",12))
    canvas.create_window(780,400,window=userentry)

    passentry=Entry(root,bd=5,width=30,relief = "ridge",font=("Calibri",12),show="•")
    canvas.create_window(780,445,window=passentry)
    
    var=IntVar()
    showbutton=Checkbutton(root,text="Show Password",bg="white",activebackground="white",font=('Playfair Display',11),borderwidth=0,variable=var,cursor="hand2",command=showpass)
    canvas.create_window(980,445,window=showbutton)

    image3 = ImageTk.PhotoImage(Image.open("login.png"))
    login=Button(root,image=image3,bg="white",activebackground="white",borderwidth=0,cursor="hand2")
    canvas.create_window(760,540,window=login)

    exitbutton=Button(root,text="EXIT",bg="white",activebackground="white",borderwidth=0,cursor="hand2",command=exit)
    canvas.create_window(768,600,window=exitbutton)

#code of splashscreen
root = Tk()
root.title("Lacaula Island")
root.iconbitmap("icon.ico")
root.geometry("600x390+460+180")
W, H=root.winfo_screenwidth(),root.winfo_screenheight()

canvas = Canvas(root)
canvas.pack(fill=BOTH, expand=True)

image11 = ImageTk.PhotoImage(Image.open("flash.png"))
canvas.create_image(300,190,image=image11)

load=Label(text="Loading...",fg="white",bg="#13253A")
canvas.create_window(300,300,window=load)
root.after(500,update)


image12 = ImageTk.PhotoImage(Image.open("circlepic.png"))
circle1=Label(image=image12,bg="#13253A")
circle2=Label(image=image12,bg="#13253A")
circle3=Label(image=image12,bg="#13253A")
circle4=Label(image=image12,bg="#13253A")
circle5=Label(image=image12,bg="#13253A")

#calling func having main screen after 5 secs
root.after(5000,come)

root.mainloop()

