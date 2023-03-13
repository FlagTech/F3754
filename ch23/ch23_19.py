from tkinter import *
from tkinter.ttk import*

app = Tk()
app.geometry('300x300')

def output():
    n, = listbox.curselection()
    text.set(listbox.get(n))
    print(listbox.curselection())
    print(listbox.selection_includes(5))
    
value = StringVar()   
value.set(('台北','東京','北京','紐約','倫敦','首爾','開羅','羅馬'))
listbox = Listbox(app,  listvariable=value)
listbox.insert(3,'坎培拉')
listbox.insert(END,'雅加達')
listbox.select_set(5)
listbox.pack()
 
btn = Button(app, text='顯示', command=output).pack()
text = StringVar()
Label(app,textvariable = text,font=("Arial",50)).pack()

app.mainloop()