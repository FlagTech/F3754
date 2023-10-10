import time

bars = r'―\|/―\|/'

print('\x1B[?25l', end='') # 隱藏游標
intervals = (0.1, 0.2, 0.3, 0.5, 0.8)
for interval in intervals:
    for char in bars:
        print(f'\r{char}', end='')
        time.sleep(interval)
print('\x1B[?25h', end='') # 顯示游標