import time
from threading import Timer
from adv_text_animator import AdvTextAnimator

class ConcurrentTextAnimator(AdvTextAnimator):
    def start(self):
        interval = self.interval
        idx = 0
        self.__timer = None
        def next_char():
            nonlocal self, interval, idx
            print(f'\r{self.txt[idx]}', end='')
            idx = (idx + 1) % len(self.txt)
            if idx == 0:
                interval *= self.easing
            self.__timer = Timer(interval, next_char)
            self.__timer.start()

        next_char()

    def stop(self):
        self.__timer.cancel()

heartbeat = ConcurrentTextAnimator(
    r'·●⬤●·●⬤●·',
    0.3,
    1     # 不變化速率
)

heartbeat.start()
print('啟動動畫', end='')
time.sleep(5)
print('停止動畫')
heartbeat.stop()
