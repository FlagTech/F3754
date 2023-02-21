import gradio as gr                       # 匯入 gradio 函式庫並簡化名稱為gr

def calculate(value1, value2):            # 建立 calculate 函式
    return value1 + value2                # 傳回兩數字相加

demo = gr.Interface(                      # 以 demo 命名建立介面
    fn=calculate,                         # 導入的函式名稱為 calculate
    inputs=['number','number'],           # 建立兩個輸入欄位為數字型態
    outputs='number',                     # 建立輸出欄位為數字型態
    title='數字總和',                      # 建立標題
    description='說明：value1 + value2 = output', # 建立說明文字
    examples=[['3854','2812']],           # 建立一組範例
    article='請點選以上範例進行測試！')      # 建立註解文章

demo.launch()                             # 啟用 demo 介面