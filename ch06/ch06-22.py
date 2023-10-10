import time

bars = r'―\|/―\|/'

for _ in range(5):
    for char in bars:
        print(f'\r{char}', end='')
        time.sleep(0.3)