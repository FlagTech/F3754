import time

class TextAnimator: # 定義名稱為 TextAnimator 的新型別
    def run(self, times):
        for _ in range(times):
            for ch in self.txt:
                print(f'\r{ch}', end='')
                time.sleep(self.interval)

bar_spinner = TextAnimator()  # 建立一個 TextAnimator 實例
bar_spinner.txt = r'―\|/―\|/' # 增加屬性：動畫文字
bar_spinner.interval = 0.3    # 增加屬性：間隔時間

TextAnimator.run(bar_spinner, 3) # 呼叫 class 中的函式
bar_spinner.run(3)               # 透過物件以方法形式呼叫 class 中的函式
