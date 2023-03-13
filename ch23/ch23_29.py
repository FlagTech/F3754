import tkinter as tk 
from tkinter.ttk import * 
from ttkthemes import ThemedTk 
from function_dict import Fractal 

root = ThemedTk(theme='breeze') # 建立視窗，並使用breeze主題
root.configure(bg="#3C3C3C") # 設定視窗背景色
root.title("樹狀碎形圖") # 設定視窗標題

# 建立主畫布，並設定大小和背景
canvas = tk.Canvas(root, width=1000, height=800, 
                   bg="#272727",highlightbackground="#272727")
canvas.grid(row=0,column=0,rowspan=30)

# 建立副畫布，並設定大小和背景
save_canvas = tk.Canvas(root, width=550, height=350, 
                        bg="#272727", highlightbackground="#272727")
save_canvas.grid(row=9, column=1,rowspan=30,columnspan=30) 

style = Style() # 建立Style物件，用來設定元件的風格和樣式
style.configure('TLabel', foreground='white',background='#3C3C3C')
style.configure('TScale', background='#3C3C3C')
style.configure('TButton', font='Helvetica 12',
                foreground='#0072E3', background='#3C3C3C')

#建立茂密程度的標籤與拉桿
label1 = Label(root,text="茂密程度")
label1.grid(row=2,column=2, columnspan=2)
scale1 = Scale(root, from_=50, to=3, orient=tk.HORIZONTAL, length=300)
scale1.set(5)
scale1.grid(row=2, column=3, columnspan=30,padx=20)

#建立樹枝長度的標籤與拉桿
label2 = Label(root,text="樹枝長度")
label2.grid(row=3,column=2, columnspan=2)
scale2 = Scale(root, from_=50, to=300, orient=tk.HORIZONTAL, length=300)
scale2.set(220)
scale2.grid(row=3, column=3, columnspan=30,padx=20)

#建立初始角度的標籤與輸入框
label3 = Label(root,text="初始角度")
label3.grid(row=4,column=2, columnspan=2)
ent1 = Entry(root,width=5)
ent1.insert(0,-90)
ent1.grid(row=4,column=3, columnspan=30)

#建立畫圖速度的標籤與拉桿
label4 = Label(root,text="畫圖速度")
label4.grid(row=5,column=2, columnspan=2)
scale3 = Scale(root, from_=200, to=1, orient=tk.HORIZONTAL, length=300)
scale3.set(50)
scale3.grid(row=5, column=3, columnspan=30,padx=20)

#建立擴散程度的標籤與拉桿
label5 = Label(root,text="擴散程度")
label5.grid(row=6,column=2, columnspan=2)
scale4 = Scale(root, from_=1, to=80, orient=tk.HORIZONTAL, length=300)
scale4.set(30)
scale4.grid(row=6, column=3, columnspan=30,padx=20)

#建立右樹枝長度的標籤與拉桿
label6 = Label(root,text="右樹枝長度")
label6.grid(row=7,column=2, columnspan=2)
scale5 = Scale(root, from_=9, to=2, orient=tk.HORIZONTAL, length=300)
scale5.set(3)
scale5.grid(row=7, column=3, columnspan=30,padx=20)

#建立左樹枝長度的標籤與拉桿
label7 = Label(root,text="左樹枝長度")
label7.grid(row=8,column=2, columnspan=2)
scale6 = Scale(root, from_=9, to=2, orient=tk.HORIZONTAL, length=300)
scale6.set(3)
scale6.grid(row=8, column=3, columnspan=30,padx=20)

#建立副畫布的標籤
label2 = Label(root,text="↓上一張",font="20")
label2.grid(row=9 ,column=2)

# 引用 function_dict 中的 Fractal 類別, 加入所需參數
app = Fractal(root,canvas,scale1,scale2,scale3,scale4,scale5,scale6,ent1)

#建立增加一層按鈕, 加入 app 中的 add 模組
button = Button(root, text="增加一層", command= lambda: app.add())
button.grid(row=0,column=2,padx=5)
#建立選擇顏色按鈕, 加入 app 中的 color_choice 模組
button = Button(root, text="選擇顏色", command=app.color_choice )
button.grid(row=0,column=3,padx=5)
#建立清除圖片按鈕, 加入 app 中的 clear 模組
button = Button(root, text="清除圖片", command=app.clear)
button.grid(row=0,column=5,padx=5)
#建立隨機樹林按鈕, 加入 app 中的 random_tree 模組
button = Button(root, text="隨機樹林", command=app.random_tree)
button.grid(row=0,column=7,padx=5)
#建立儲存圖片按鈕, 加入 app 中的 openfile 模組
button = Button(root, text="儲存圖片", command=app.openfile)
button.grid(row=0,column=9,padx=5)
#當按下 Enter 鍵則觸發 app 中的 animate 模組
root.bind('<Return>', app.animate)
#更換應用程式圖示
root.iconbitmap('C:\\Users\\Admin\\Desktop\\工作\\FXXX\\範例檔案\\ch23\\upload\\tree_icon.ico')

root.mainloop()