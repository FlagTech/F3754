import gradio as gr             # 匯入 gradio 函式庫並簡化名稱為gr

def imshow(image):              # 建立 imshow 函式
    print(type(image),image)    # 輸出影像資料型態與影像資料
    return image                # 傳回影像

demo = gr.Interface(            # 以 demo 命名建立介面
    fn=imshow,                  # 導入的函式名稱為 imshow
    inputs=gr.Image(),          # 建立影像輸入欄位
    outputs=gr.Image())         # 建立影像輸出欄位

demo.launch()                   # 啟用 demo 介面