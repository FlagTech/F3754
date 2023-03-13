import tkinter as tk
from tkinter.ttk import*

app = tk.Tk()
app.geometry('500x200')

style = Style()
Button(app, text='button_1').pack()
Button(app, text='button_2').pack(pady=5)
Button(app, text='button_3').pack(pady=10)
Button(app, text='button_4').pack(pady=25)

app.mainloop()