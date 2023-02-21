import gradio as gr                # 匯入 gradio 函式庫並簡化名稱為gr

def hello(name):                   # 建立 hello 函式
    ans = "Hello " + name + "!\nI am Gradio!"
    return ans                     # 傳回字串

demo = gr.Interface(               # 以 demo 命名建立介面
    fn=hello,                      # 導入的函式名稱為 hello
    # 建立輸入欄位, 至少5行的高度，提示字元為 Input name
    inputs=gr.Textbox(lines=5, placeholder="Input name",label="你的名字"),
    outputs=gr.Textbox(lines=5,label="Gradio"),   # 建立輸出欄位, 至少5行的高度
    title="Hello I am Gradio!")

demo.launch()                      # 啟用 demo 介面