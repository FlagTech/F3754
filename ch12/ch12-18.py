import time

class TextAnimator: # 定義名稱為 TextAnimator 的新型別
    @property
    def interval(self):
        return self.__interval

    @interval.setter
    def interval(self, interval):
        self.__interval = interval if interval > 0 else 0

    def __init__(self, txt, interval):
        self.txt = txt               # 動畫文字
        self.interval = interval   # 間隔時間

    def run(self, times):
        for _ in range(times):
            for ch in self.txt:
                print(f'\r{ch}', end='')
                time.sleep(self.interval)

    def __repr__(self):
        return (f'{self.__class__.__name__}(\n'
                f'    {self.txt!r}, \n'
                f'    {self.interval!r}, \n'
                f')')
    
    def __str__(self):
        return (f"以 '{self.txt}' 間隔 {self.interval:.2f} 秒顯示動畫")
    
    def __bool__(self):
        return self.interval > 0 and len(self.txt) > 1

bar_spinner = TextAnimator( # 建立物件同時可以設定屬性
    r'―\|/―\|/',
    0.3
)

print(bool(bar_spinner))
bar_spinner.interval = -3
print(bool(bar_spinner))
bar_spinner.interval = 1.5
bar_spinner.txt = '|'
print(bool(bar_spinner))