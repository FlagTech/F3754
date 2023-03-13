from tkinter import *
from tkinter.ttk import*

app = Tk()
app.geometry('600x300')

canvas = Canvas(app, width=600, height=300,bg='#D6D6AD')
canvas.pack()
canvas.create_text(180, 120, text='I Love Python',
                   anchor='nw', fill='green', font=('Arial', 30))
for i in range(0,150,10):
    canvas.create_line(i, 0, 200, 200+i, width=4, fill='#00BB00', dash=(10,2))
    canvas.create_line(590-i, 0, 400, 200+i, width=4, fill='#00BB00', dash=(10,2))
    
app.mainloop()