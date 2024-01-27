import text_animator
import time

class AdvTextAnimator(text_animator.TextAnimator):
    def ease_out(self, times):
        interval = self.interval
        for _ in range(times):
            for ch in self.txt:
                print(f'\r{ch}', end='')
                time.sleep(interval)
            interval *= 1.5  # 加長間隔時間 1.5 倍

heartbeat = AdvTextAnimator( # 建立子類別的物件
    r'·●⬤●·●⬤●·',           # 透過父類別設定初值的方法
    0.3
)
heartbeat.run(3) # 一樣可以使用父類別中定義的方法
heartbeat.ease_out(3)   # 心跳到停止的感覺