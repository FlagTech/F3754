import time

def start_timer():
    start_time = time.perf_counter_ns()
    try:
        while True:
            elapsed_time = time.perf_counter_ns() - start_time
            start_time = time.perf_counter_ns()
            yield elapsed_time
    except ValueError:
        print('因意外因素關閉計時器')
        yield elapsed_time

timer = start_timer()
next(timer) # 啟動 timer
time.sleep(1)
print(timer.throw(ValueError())) # 關閉 timer