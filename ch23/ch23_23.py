from tkinter import *
from tkinter.ttk import*
from PIL import Image, ImageTk

app = Tk()
app.geometry('800x650')

img = Image.open('圖片檔案路徑')
imgtk = ImageTk.PhotoImage(img)

canvas = Canvas(app, width=800, height=650)
canvas.create_image(0, 0, anchor='nw', image=imgtk)
canvas.pack()

app.mainloop()