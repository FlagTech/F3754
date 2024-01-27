import time

class TextAnimator: # 定義名稱為 TextAnimator 的新型別
    def __init__(self, txt, interval):
        self.txt = txt               # 動畫文字
        self.__interval = interval   # 間隔時間

    @property
    def interval(self):
        return self.__interval

    @interval.setter   # 可設定 interval 屬性的方法
    def interval(self, interval):
        self.__interval = interval if interval > 0 else 0

    def run(self, times):
        for _ in range(times):
            for ch in self.txt:
                print(f'\r{ch}', end='')
                time.sleep(self.__interval)

bar_spinner = TextAnimator( # 建立物件同時可以設定屬性
    r'―\|/―\|/',
    0.3
)

print(bar_spinner._TextAnimator__interval) # 讀取屬性
bar_spinner.interval = 0.8
print(bar_spinner._TextAnimator__interval) # 確認屬性
bar_spinner.run(3)