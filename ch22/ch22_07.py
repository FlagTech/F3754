import gradio as gr                # 匯入 gradio 函式庫並簡化名稱為gr

def options(option):               # 建立 options 函式
    option = option-1911           # 西元年轉民國年
    return option                  # 傳回數值

demo = gr.Interface(               # 以 demo 命名建立介面
    fn=options,                    # 導入的函式名稱為 options
    # 建立下拉式選單, 列出1911到2024的年份
    inputs=gr.Dropdown(choices=list(range(2024, 1911, -1)),
                       label="請選擇西元出生年份"),
    outputs=gr.Text(label='你的民國出生年份'), # 建立文本輸出欄位
    title="西元年轉民國年")          # 標題

demo.launch()                      # 啟用 demo 介面