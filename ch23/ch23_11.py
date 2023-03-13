import tkinter as tk
from tkinter.ttk import*

app = tk.Tk()
app.geometry('300x500')

style = Style()
Button(app, text='CENTER').pack()
Button(app, text='東').pack(anchor=tk.E)
Button(app, text='西').pack(anchor=tk.W)

tk.Label(app, text="東北",height=5,width=10,
         bg="white",anchor=tk.NE).pack(pady=5)
tk.Label(app, text="東南",height=5,width=10,
         bg="white",anchor=tk.SE).pack(pady=5)
tk.Label(app, text="西南",height=5,width=10,
         bg="white",anchor=tk.SW).pack(pady=5)
tk.Label(app, text="西北",height=5,width=10,
         bg="white",anchor=tk.NW).pack(pady=5)
app.mainloop()