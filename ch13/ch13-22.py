from threading import Timer
import time

count = 0
timer = None

def counting():
    global count, timer
    print(f'\r{count}', end='')
    count += 1
    timer = Timer(0.5, counting)
    timer.start()
counting()
print('開始計數')
time.sleep(5)
timer.cancel()
print('停止計數')