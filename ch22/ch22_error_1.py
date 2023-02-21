import gradio as gr                 # 匯入 gradio 函式庫並簡化名稱為gr

def hello(arg1,arg2):               # 建立 hello 函式, 共兩個參數
    return arg1,arg2                # 傳回字串

demo = gr.Interface(fn=hello,       # 以 demo 命名建立介面
                    inputs=["text","text","text","text"], #  總共4個輸入元件
                    outputs="text") # 輸出1個元件
demo.launch()                       # 啟用 demo 介面