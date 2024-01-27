import time

class TextAnimator: # 定義名稱為 TextAnimator 的新型別
    def __init__(self, txt, interval):
        self.txt = txt             # 動畫文字
        self.interval = interval   # 間隔時間

    def run(self, times):
        for _ in range(times):
            for ch in self.txt:
                print(f'\r{ch}', end='')
                time.sleep(self.interval)

bar_spinner = TextAnimator( # 建立物件同時可以設定屬性
    r'―\|/―\|/',
    0.3
)
bar_spinner.run(3) # 不同效果的動畫用不同名稱的物件表示

heartbeat = TextAnimator(  # 建立物件同時可以設定屬性
    r'·●⬤●·●⬤●·',
    0.2
)
heartbeat.run(3)   # 心跳的感覺
