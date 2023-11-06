import time

def text_animation(chars, *intervals):
    for interval in intervals:
        for char in chars:
            print(f'\r{char}', end='')
            time.sleep(interval)

text_animation(r'―\|/―\|/', 0.2, 0.3, 0.5, 0.8)