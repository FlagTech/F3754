import tkinter as tk
from tkinter.ttk import*

app = tk.Tk()
app.geometry("300x200")
style = Style()

print('所有主題:',style.theme_names())
#style.theme_use("winnative")
print('目前主題:',style.theme_use())

Label(app, text="Hello tkinter").pack()
Button(app, text="hello tkinter").pack(pady=10)

app.mainloop()