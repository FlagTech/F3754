import tkinter as tk
from tkinter.ttk import*

app = tk.Tk()
app.geometry('300x200')
app.title("輸入框")
app.configure(bg="white")

user_input = tk.StringVar()  
user_input.set('')            

Entry(app,textvariable=user_input,width=20).pack()
Label(app,textvariable=user_input,width=20).pack()

app.mainloop()