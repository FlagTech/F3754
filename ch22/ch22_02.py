import gradio as gr                # 匯入 gradio 函式庫並簡化名稱為gr

def hello(name):                   # 建立 hello 函式
    return "Hello " + name + "!"   # 傳回字串
# 以 demo 命名建立介面
demo = gr.Interface(fn=hello, inputs="text",outputs="text") 

demo.launch()                      # 啟用 demo 介面