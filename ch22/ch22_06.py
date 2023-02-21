import gradio as gr                # 匯入 gradio 函式庫並簡化名稱為gr

def options(option):               # 建立 options 函式
    return "你選擇了 "+option       # 傳回字串

demo = gr.Interface(               # 以 demo 命名建立介面
    fn=options,                    # 導入的函式名稱為 options
    inputs=gr.Radio(["香蕉", "蘋果", "芭樂"],value="蘋果"), # 建立單選鈕
    outputs="text")                # 建立文本輸出欄位

demo.launch()                      # 啟用 demo 介面