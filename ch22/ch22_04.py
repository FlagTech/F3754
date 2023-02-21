import gradio as gr                           # 匯入 gradio 函式庫並簡化名稱為gr

def hello(name):                              # 建立 hello 函式
    return "Hello "+ name +'!'                # 傳回字串

demo = gr.Interface(                          # 以 demo 命名建立介面
    fn=hello,                                 # 導入的函式名稱為 hello
    inputs="text",                            # 建立文本輸入欄位
    outputs="text",                           # 建立文本輸出欄位
    title="歡迎來到 Gradio！")                 # 建立標題

# 啟用 demo 介面, 設定為公開網頁,建立一組使用者帳號與密碼
demo.launch(share=True,auth=("user","123"))   