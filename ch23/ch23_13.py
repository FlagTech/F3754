import tkinter as tk
from tkinter.ttk import*

app = tk.Tk()
app.geometry('300x200')

style = Style()
Button(app, text="東").place(relx=0.5, rely=0.5, anchor="e")
Button(app, text="西").place(relx=0.5, rely=0.5, anchor="w")
Button(app, text="北").place(relx=0.5, rely=0.6, anchor="n")
Button(app, text="南").place(relx=0.5, rely=0.4, anchor="s",
                            relheight=0.2, relwidth=0.2)
app.mainloop()