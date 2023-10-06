import time

bars = '―\|/―\|/'

for char in bars:
    print(f'\r{char}', end='')
    time.sleep(0.3)