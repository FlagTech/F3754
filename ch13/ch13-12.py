import text_animator
import time

class AdvTextAnimator(text_animator.TextAnimator):
    # 定義變化倍數屬性
    @property
    def easing(self):
        return self.__easing

    @easing.setter
    def easing(self, easing):
        self.__easing = easing if easing > 0 else 1

    def __init__(self, txt, interval, easing):
        self.easing = easing
        # 使用父類別定義的方法設定初值
        super().__init__(txt, interval)

    def ease_out(self, times):
        interval = self.interval
        for _ in range(times):
            for ch in self.txt:
                print(f'\r{ch}', end='')
                time.sleep(interval)
            interval *= self.easing  # 加長間隔時間

    def __repr__(self):
        return (f'{self.__class__.__name__}(\n'
                f'    {self.txt!r}, \n'
                f'    {self.interval!r}, \n'
                f'    {self.easing!r}, \n'
                f')')
    
    def __str__(self):
        return (super().__str__() +
                f" (每輪調速 {self.easing:.2f} 倍)")

    def __eq__(self, obj):
        print("child's __eq__ called")
        if (result := super().__eq__(obj)) is NotImplemented:
            return NotImplemented
        return (result # 動畫字串與時間間隔相同
                and isinstance(obj, __class__)
                and (self.easing == obj.easing))

    def __lt__(self, obj):
        print("child's __lt__ called")
        if super().__lt__(obj) is NotImplemented:
            return NotImplemented
        obj_easing = 1
        # 同類別或是子類別實例才具備 easing 屬性
        if isinstance(obj, __class__):
            obj_easing = obj.easing
        return (self.easing < obj_easing)

    def __gt__(self, obj):
        print("child's __gt__ called")
        return not (self == obj or self < obj)

bar_spinner1 = text_animator.TextAnimator(
    r'―\|/―\|/', 
    0.3
)
        
bar_spinner2 = AdvTextAnimator(
    r'―\|/―\|/', 
    0.3,
    1.5
)

bar_spinner3 = AdvTextAnimator(
    r'―\|/―\|/', 
    0.3,
    0.1
)
print(bar_spinner1 < bar_spinner2)
print(bar_spinner2 < bar_spinner3)
print(bar_spinner3 < bar_spinner1)