import time

def start_timer():
    start_time = time.perf_counter_ns()
    while True:
        elapsed_time = time.perf_counter_ns() - start_time
        start_time = time.perf_counter_ns()
        reset = yield elapsed_time
        if reset: # 如果有 reset 則重設開始時間
            start_time = time.perf_counter_ns()

timer = start_timer()
next(timer) # 啟動 timer
time.sleep(3)
print(f'重設後經過 {timer.send(True)} 奈秒')
time.sleep(1)
print(f'經過 {next(timer)} 奈秒')