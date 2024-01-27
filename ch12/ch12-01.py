import time

def text_animation(txt, interval, repeat):
    for _ in range(repeat):
        for ch in txt:
            print(f'\r{ch}', end='')
            time.sleep(interval)


text_animation(
    r'―\|/―\|/',   # 動畫文字
    0.3,           # 間隔時間
    3              # 循環次數
)