import time

bars = r'―\|/―\|/'

for i in range(len(bars)):
    print(f'\r{bars[i]}', end='')
    time.sleep(0.3)

for i in range(len(bars)):
    print(f'\r{bars[i]}', end='')
    time.sleep(0.5)

for i in range(len(bars)):
    print(f'\r{bars[i]}', end='')
    time.sleep(0.8)