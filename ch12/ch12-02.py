import time

def text_animation(txt, interval, repeat):
    for _ in range(repeat):
        for ch in txt:
            print(f'\r{ch}', end='')
            time.sleep(interval)

def bar_animation(interval, repeat):
    bars = r'―\|/―\|/'
    text_animation(bars, interval, repeat)
    
def circle_animation(interval, repeat):
    circles = '◑◒◐◓◑◒◐◓'
    text_animation(circles, interval, repeat)
    
bar_animation(
    0.3,          # 間隔時間
    3             # 循環次數
)

circle_animation(
    0.3,          # 間隔時間
    3             # 循環次數
)