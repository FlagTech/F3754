import tkinter as tk

app = tk.Tk()
app.geometry("300x200")

def func(event):
    print("You hit return.")
app.bind('<Return>', func)

app.mainloop()