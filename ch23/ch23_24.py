from tkinter.ttk import*
from ttkthemes import ThemedTk

app = ThemedTk(theme='breeze')
print(app.get_themes())
app.geometry('500x200')

Label(app,text="Label").pack()
Button(app, text='button').pack()
Scale(app,length=300).pack()
Entry(app).pack()

app.mainloop()