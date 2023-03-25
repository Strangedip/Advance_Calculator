import tkinter 
from tkinter import * 


### for creating main manu
manu= Tk()
manu.title('Strange Calculator')
manu.geometry('285x394+700+200')
manu.resizable(False,False)
manu.config(bg="#e3f4f1")

def open():
    manu.destroy()
    import main

Button(manu,text='Open Calculator',command=open).place(relx=0.5,rely=0.5,anchor=CENTER)

manu.mainloop()

