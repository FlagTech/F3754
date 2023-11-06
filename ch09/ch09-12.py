import time

def text_animation(chars, *intervals, repeats=1):
    for _ in range(repeats):
        for interval in intervals:
            for char in chars:
                print(f'\r{char}', end='')
                time.sleep(interval)

# 2 會被當成位置引數收入 intervals 序組中
text_animation(r'―\|/―\|/', 0.3, 2)
# repeats 一定要使用指名引數才能傳入
text_animation(r'―\|/―\|/', 0.3, repeats=2)