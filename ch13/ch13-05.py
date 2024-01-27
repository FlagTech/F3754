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

heartbeat = AdvTextAnimator( # 建立子類別的物件
    r'·●⬤●·●⬤●·',           
    0.3,
    1.5
)
heartbeat.easing = 0.9
print(heartbeat.easing)
heartbeat.ease_out(3)