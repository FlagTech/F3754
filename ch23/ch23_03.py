import tkinter as tk
from tkinter.ttk import*

app = tk.Tk()
app.geometry('300x200')

def hello():
    Button(app, text="hello!").pack()

Button(app, text='button',
       width="20",
       command=hello).pack()

app.mainloop()