import time

def start_timer():
    start_time = time.perf_counter_ns()
    while True:
        elapsed_time = time.perf_counter_ns() - start_time
        start_time = time.perf_counter_ns()
        yield elapsed_time

timer = start_timer()
next(timer) # 啟動 timer
time.sleep(1)
timer.close() # 關閉 timer
print(f'經過 {next(timer)} 奈秒')