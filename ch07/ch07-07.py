import time

bars = r'―\|/―\|/'
intervals = 0.1, 0.2, 0.3, 0.5, 0.8

for interval in intervals:
    for i in range(len(bars)):
        print(f'\r{bars[i]}', end='')
        time.sleep(interval)