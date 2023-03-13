import tkinter as tk
from tkinter.ttk import*
from tkinter.colorchooser import*
from tkinter.filedialog import*
from ttkthemes import ThemedTk
import random
import math
import time
from PIL import Image, ImageGrab, ImageTk
import win32gui


class Fractal:
    def __init__(self, master,canvas,scale1,scale2,scale3,scale4,scale5,scale6,ent1):
        self.root = None
        self.master = master
        self.color = None
        self.length_value = 220
        self.depth = 0
        self.angle_value = -90
        self.depth_value = 5
        self.animation_speed = 100 # 可以調整動畫的速度
        self.angle_change = 30
        self.wright_length = self.left_length = 0
        self.scale1 = scale1
        self.scale2 = scale2
        self.scale3 = scale3
        self.scale4 = scale4
        self.scale5 = scale5
        self.scale6 = scale6
        self.ent1 = ent1
        self.canvas = canvas
        img = Image.new("RGB", (450, 320), color="#272727")
        img.save("./canvas.jpeg")
        self.original_image = Image.open("./canvas.jpeg")
        self.cropped_image = self.original_image.crop((0, 0, 450, 320))
        self.photo_image = ImageTk.PhotoImage(self.cropped_image)
        self.save_canvas = tk.Canvas(master, width=450, height=320, bg="#272727", highlightbackground="#272727")
        self.save_canvas.create_image(0, 0, image=self.photo_image, anchor=tk.NW)
        self.save_canvas.grid(row=9, column=1,rowspan=30,columnspan=30)
        
        
    def draw_tree(self,x1,y1, angle=None, length=None,color="white"):
        if x1 is None:
            x1 = self.x1
            
        if y1 is None:
            y1 = self.y1
        
        if length is None:
            length = int(self.length_value)
        
        if angle is None:
            angle = int(self.angle_value)
        
        if length < int(self.depth_value):
            return
        
        if length < 60 and self.color!=None:
            color=self.color

        if self.depth == 5:
            return

        x2 = x1 + length * math.cos(math.radians(angle))
        y2 = y1 + length * math.sin(math.radians(angle))
        
        # 繪製樹枝
        self.canvas.create_line(x1, y1, x2, y2, fill=color)

        # 繪製左樹枝
        self.depth += 1
        self.master.after(self.animation_speed, self.draw_tree, x2, y2, angle + random.uniform(-(self.angle_change), -10), length*(0.7+((3-self.left_length)*0.1)))
        self.depth -= 1

        # 繪製右樹枝
        self.depth += 1
        self.master.after(self.animation_speed, self.draw_tree, x2, y2, angle + random.uniform(10, self.angle_change), length*(0.7+((3-self.wright_length)*0.1)))
        self.depth -= 1
    
    def openfile(self):
        file = tk.filedialog.asksaveasfilename()
        if "jpeg" not in file:
            file += ".jpeg"
        self.CaptureScreen(file)
        
    def CaptureScreen(self,Location):
        Focus = win32gui.GetFocus()
        coordinate=win32gui.GetWindowRect(Focus)
        x_coord = coordinate[0]
        x1_coord=x_coord+self.canvas.winfo_width()
        y_coord = coordinate[1]
        y1_coord=y_coord+self.canvas.winfo_height()
        im=ImageGrab.grab((x_coord,y_coord,x1_coord,y1_coord))
        im.save(Location,'jpeg')    

    def rountine(self,num):
        self.depth = 0
        self.depth_value = self.scale1.get()
        self.angle_value = self.ent1.get()
        self.animation_speed = round(self.scale3.get())
        self.length_value = self.scale2.get()
        self.angle_change = self.scale4.get()
        self.wright_length = self.scale5.get()
        self.left_length = self.scale6.get()
        if num == 1:
            self.canvas.delete("all")
        self.draw_tree(x1=500,y1=750)
        self.CaptureScreen("./canvas.jpeg")
        self.original_image = Image.open("./canvas.jpeg")
        self.cropped_image = self.original_image.resize((450, 320))
        self.photo_image = ImageTk.PhotoImage(self.cropped_image)
        self.save_canvas.create_image(0, 0, image=self.photo_image, anchor=tk.NW)
    
    def animate(self,event):
        self.rountine(1)
    
    def add(self):
        self.rountine(0)
        
    def color_choice(self):
        (n,color) = tk.colorchooser.askcolor()
        self.color=color
    
    def clear(self):
        self.canvas.delete("all")
    
    def random_tree(self):
        self.depth = 0
        self.angle_change = self.scale4.get()
        self.wright_length = self.scale5.get()
        self.left_length = self.scale6.get()
        for i in range(20):
            self.depth_value = random.randint(8,10)
            self.angle_value = -(random.randint(85,95))
            self.animation_speed = 1
            self.length_value = random.randint(50,300)
            self.draw_tree(x1=random.randint(50,1050),y1=random.randint(300,800))