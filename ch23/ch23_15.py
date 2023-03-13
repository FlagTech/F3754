import tkinter as tk
from tkinter.ttk import*

def user_text(en1):
    Label(app,text=en1.get(),width=20).grid(row=1,column=0)
    
app = tk.Tk()
app.geometry('300x200')
app.title("輸入框")
app.configure(bg="white")

en1 = Entry(app,width=20)
en1.grid(row=0,column=0)
Button(app,text='按鈕',command=lambda:user_text(en1)).grid(row=0,column=1)

app.mainloop()