import gradio as gr                # 匯入 gradio 函式庫並簡化名稱為gr

def options(option):               # 建立 options 函式
    option = round(option*9/5+32,1)
    return option                  # 傳回數值

demo = gr.Interface(               # 以 demo 命名建立介面
    fn=options,                    # 導入的函式名稱為 options
    # 建立輸入滑桿, 範圍(0~100), 初始值50, 設定欄位標題
    inputs=gr.Slider(minimum=0,maximum=100,
                     value=50,label="請設定現在的攝氏溫度"),
    # 建立輸出滑桿, 範圍(0~200), 設定欄位標題
    outputs=gr.Slider(minimum=0,maximum=250,label='華氏溫度'),
    title="攝氏轉華氏溫度：")        # 標題

demo.launch()                      # 啟用 demo 介面