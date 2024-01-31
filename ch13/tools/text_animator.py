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
    
    def __eq__(self, obj):
        print('__eq__ called')
        if not isinstance(obj,  __class__):
            return NotImplemented
        return (self.interval == obj.interval 
                and self.txt == obj.txt)

    def __lt__(self, obj):
        print('__lt__ called')
        if not isinstance(obj,  __class__):
            return NotImplemented
        return (self.interval * len(self.txt) 
                < obj.interval * len(obj.txt))

    def __mul__(self, times):
        print('__mul__ called')
        if not isinstance(times, (int, float)):
            return NotImplemented
        return TextAnimator(self.txt, self.interval * times)

    def __rmul__(self, times):
        print('__rmul__ called')
        return self.__mul__(times)

    def __imul__(self, times):
        print('__imul__ called')
        self.interval *= times
        return self

if __name__ == '__main__':
    bar_spinner = TextAnimator( # 建立物件同時可以設定屬性
        r'―\|/―\|/',
        0.3
    )

    bar_spinner = bar_spinner * 3
    print(f'{id(bar_spinner)}:{bar_spinner}')
    bar_spinner = 0.5 * bar_spinner
    print(f'{id(bar_spinner)}:{bar_spinner}')
    bar_spinner *= 2
    print(f'{id(bar_spinner)}:{bar_spinner}')
