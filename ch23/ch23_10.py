import tkinter as tk
from tkinter.ttk import*

app = tk.Tk()
app.geometry('300x200')

style = Style()
Button(app, text='button1',
       width="20").pack(fill="x")
Button(app, text='button2',
       width="20").pack(fill="y", side='right')
Button(app, text='button3',
       width="20").pack(fill="y", expand=1)
Button(app, text='button4',
       width="20").pack(pady=20, padx=20)
app.mainloop()