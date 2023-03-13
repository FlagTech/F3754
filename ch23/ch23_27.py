from ttkthemes import ThemedTk

app = ThemedTk(theme='breeze')
app.geometry('300x200')
app.configure(bg="#3C3C3C")
app.title("樹狀碎形圖") 
app.iconbitmap('檔案路徑')

app.mainloop()