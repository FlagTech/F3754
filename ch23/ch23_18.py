from tkinter import *
from tkinter.ttk import*

app = Tk()
app.geometry('300x200')

direction = StringVar()
btn1 = Radiobutton(app, text='left',variable=direction, value='左')
btn1.grid(row=0,column=0)

btn2 = Radiobutton(app, text='mid',variable=direction, value='中')
btn2.grid(row=0,column=1)

btn3 = Radiobutton(app, text='right',variable=direction, value='右')
btn3.grid(row=0,column=2)

btn2.invoke()
btn3.configure(state = DISABLED)
Label(app,textvariable=direction,font=("Arial",50)).grid(row=1,column=1)
app.mainloop()