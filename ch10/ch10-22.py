import time

def start_timer(laps):
    start_time = time.perf_counter_ns()
    for i in range(laps):
        elapsed_time = time.perf_counter_ns() - start_time
        start_time = time.perf_counter_ns()
        yield elapsed_time

for elapsed_time in start_timer(3):
    print(f'經過 {elapsed_time} 奈秒')
    time.sleep(1)