import time

def start_timer():
    start_time = time.perf_counter_ns()
    def end_timer():
        elapsed_time = time.perf_counter_ns() - start_time
        # 指派名稱會建立區域的名稱
        start_time = time.perf_counter_ns()
        return elapsed_time
    return end_timer

elapsed_time = start_timer()
time.sleep(1)
print(f'經過 {elapsed_time()} 奈秒')