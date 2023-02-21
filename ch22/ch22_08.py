import gradio as gr                    # 匯入 gradio 函式庫並簡化名稱為gr

def options(op1,op2,op3,op4,op5):      # 建立 options 函式
    ans = [True,False,False,True,True] # 正確解答
    user = [op1,op2,op3,op4,op5]       # 使用者的答案
    if ans == user:                    # 如果正確則回傳答對字串
        return "恭喜答對!\n依次排名為:\n哈里發塔 > 默迪卡118 > 上海中心大廈"
    else: return "回答錯誤"             # 如果錯誤則回傳錯誤字串

demo = gr.Interface(                   # 以 demo 命名建立介面
    fn=options,                        # 導入的函式名稱為 options
    # 建立核取方塊, 共有五個輸入區域
    inputs=[gr.Checkbox(label="哈里發塔"),gr.Checkbox(label="東京晴空塔"),
            gr.Checkbox(label="台北101"),gr.Checkbox(label="上海中心大廈"),
            gr.Checkbox(label="默迪卡118")],
    outputs="text",                    # 建立文本輸出框
    title="世界最高建築",               # 標題
    description="猜猜看以下哪三個是世界排行前三高的建築")  # 說明文字

demo.launch()                          # 啟用 demo 介面