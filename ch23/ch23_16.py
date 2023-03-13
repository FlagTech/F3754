import tkinter as tk
from tkinter.ttk import*

app = tk.Tk()
app.geometry('200x200')

style = Style()
style.configure("test.TFrame",background="black")
frame1 = Frame(app,style="test.TFrame",padding=(3,3,3,3))               
frame2 = Frame(app,style="test.TFrame",padding=(3,3,3,3))          
frame1.pack()
frame2.pack()
Button(frame1, text='Frame1').pack()
Button(frame2, text='Frame2').pack()

app.mainloop()