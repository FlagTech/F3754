import tkinter as tk
from tkinter.ttk import*

app = tk.Tk()
app.geometry('500x200')

style = Style()
Button(app, text='button_1').pack(side="left")
Button(app, text='button_2').pack(side="left",padx=5)
Button(app, text='button_3').pack(side="left",padx=10)
Button(app, text='button_4').pack(side="left",padx=25)

app.mainloop()