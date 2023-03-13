import tkinter as tk
from tkinter.ttk import*

app = tk.Tk()
app.geometry('300x200')

style = Style()
Button(app, text='A00').grid(row=0,column=0)
Button(app, text='A10').grid(row=1,column=0)
Button(app, text='A20').grid(row=2,column=0)
Button(app, text='A01').grid(row=0,column=1)
Button(app, text='A11').grid(row=1,column=1)
Button(app, text='A21').grid(row=2,column=1)
Button(app, text='GO!').grid(row=0,column=2,rowspan=3,ipady=25)
app.mainloop()