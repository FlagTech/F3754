from tkinter import *
from tkinter.ttk import*

app = Tk()
app.geometry('300x150')

frame = Frame(app,width=20)
frame.pack()
scrollbar = Scrollbar(frame)        
scrollbar.pack(side='right', fill='y')  

value = StringVar()
value.set(('台北','東京','北京','紐約','倫敦','首爾','開羅','羅馬'))

listbox = Listbox(frame, listvariable=value, height=6,
                  width=15, yscrollcommand=scrollbar.set)
listbox.pack()    
scrollbar.config(command = listbox.yview)  

app.mainloop()