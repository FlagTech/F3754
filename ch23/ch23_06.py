import tkinter as tk
from tkinter.ttk import*

app = tk.Tk()
app.geometry('300x200')

style = Style()
Button(app, text='button').pack()
Button(app, text='button_top').pack(side="top")
Button(app, text='button_bottom').pack(side="bottom")
Button(app, text='button_left').pack(side="left")
Button(app, text='button_right').pack(side="right")

app.mainloop()