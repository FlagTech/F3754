import time

def start_timer():
    start_time = time.perf_counter_ns()
    def end_timer():
        nonlocal start_time # 使用上層名稱
        elapsed_time = time.perf_counter_ns() - start_time
        start_time = time.perf_counter_ns()
        return elapsed_time
    return end_timer

elapsed_time = start_timer()
time.sleep(1)
print(f'經過 {elapsed_time()} 奈秒')
time.sleep(1)
print(f'經過 {elapsed_time()} 奈秒')