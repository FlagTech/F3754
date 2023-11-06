import time

def text_animation(chars, interval, repeats=1):
    for _ in range(repeats):
        for char in chars:
            print(f'\r{char}', end='')
            time.sleep(interval)

text_animation(r'―\|/―\|/', 0.3, 3)