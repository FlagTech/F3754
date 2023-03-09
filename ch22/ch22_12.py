import gradio as gr  # 匯入 gradio 函式庫並簡化名稱為gr
from ch22_11 import flower_book

demo = gr.Interface(
    fn=flower_book,
    inputs=gr.Textbox(lines=2, label="花名", placeholder="輸入花名"),
    outputs=gr.Textbox(lines=2, label="花語", placeholder="顯示相關花語"),
    title="花語事典",
    examples=[["玫瑰"],["向日葵"],["百合"],["薰衣草"],["薔薇"],
              ["康乃馨"],["水仙花"],["小蒼蘭"],["鬱金香"]],
    description="這是一個花語查詢器,"
                "輸入花名後會顯示相關的花語, 可以按一下範例查詢")

demo.launch()