import tkinter as tk
from tkinter.ttk import*

app = tk.Tk()
app.geometry("300x200")

style = Style()
style.configure('test.TLabel', font='Times 20',
                foreground='white', background="#006000")
style.configure('test.TButton', font='Times 20',padding=15,
                foreground='black', background="#A6FFFF")

Label(app, text="hello tkinter",
      style='test.TLabel').pack()
Button(app, text="Go!",
      style='test.TButton').pack(pady=10)

app.mainloop()