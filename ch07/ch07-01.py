import time

bars = r'―\|/―\|/'

for interval in range(3, 6):
    for i in range(len(bars)):
        print(f'\r{bars[i]}', end='')
        time.sleep(interval / 10)