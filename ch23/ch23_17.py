from tkinter import *
from tkinter.ttk import*

app = Tk()

def new():
    print("開新檔案")
def old():
    print("開啟舊檔")
menu = Menu(app)

menubar = Menu(menu,tearoff=0)
menubar.add_command(label="開新檔案",command=new)
menubar.add_command(label="開啟舊檔",command=old)
menubar.add_separator()

menubar2 = Menu(menu,tearoff=0)
menubar2.add_command(label="檔案1")
menubar2.add_command(label="檔案2")
menubar.add_cascade(label="最近編輯的檔案", menu=menubar2)

menu.add_cascade(label="檔案",menu=menubar)
menu.add_cascade(label="編輯")
app.config(menu=menu)
app.mainloop()