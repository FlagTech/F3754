import tkinter as tk
app = tk.Tk()

app.geometry("500x300")
tk.Label(app, text="Hello Tkinter!",
         width="20",
         height="10",
         bg="white",
         font=("Arial", 25),
         relief="solid").pack()

app.mainloop()