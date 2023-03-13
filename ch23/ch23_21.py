from tkinter import *
from tkinter.ttk import*
app = Tk()
app.geometry('500x200')
def value():
    print(scale.get())
scale = Scale(app,from_=0,to=300,length=300)
scale.pack()
Button(app, text='button',command=value).pack()
app.mainloop()