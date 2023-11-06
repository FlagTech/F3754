import time

def start_timer():
    start_time = time.perf_counter_ns()
    def end_timer():
        return time.perf_counter_ns() - start_time
    return end_timer

elapsed_time1 = start_timer()
time.sleep(1) # 假裝在做事
elapsed_time2 = start_timer()
print(f'經過 {elapsed_time1()} 奈秒')
print(f'經過 {elapsed_time2()} 奈秒')