import tkinter as tk
from tkinter.ttk import*

app = tk.Tk()
app.geometry('300x200')

style = Style()
Button(app, text='button').pack()
Button(app, text='button_ix').pack(ipadx=10)
Button(app, text='button_iy').pack(ipady=10)

app.mainloop()