import time

def text_animation(chars, *intervals, **config):
    repeats = config.get('repeats', 1) # 要記得設定預設值
    reverse = config.get('reverse', False)
    for _ in range(repeats):
        for interval in intervals:
            for char in chars:
                print(f'\r{char}', end='')
                time.sleep(interval)
        if reverse: chars = chars[::-1]

text_animation(
    r'―\|/―\|/', 0.2, 0.3, 0.5,
    # 可以隨意傳入任意數量的指名參數
    reverse=True, repeats=2)