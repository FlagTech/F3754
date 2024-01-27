import text_animator
import time

class AdvTextAnimator(text_animator.TextAnimator):
    __default = None

    def get_default():
        if not AdvTextAnimator.__default:
            AdvTextAnimator.__default = AdvTextAnimator(
                r'―\|/―\|/',
                0.1,
                1.5
            )
        return AdvTextAnimator.__default
        
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

# 取得預設的動畫效果物件
bar_spinner = AdvTextAnimator.get_default()
bar_spinner.run(3)