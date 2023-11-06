import time

def fib_performance(fib, n):
    start = time.perf_counter_ns()
    fib(n)
    end = time.perf_counter_ns()
    return end - start

def fib(n):
    # 停止遞迴的條件
    if n == 0: return 0
    if n == 1: return 1
    return fib(n - 1) + fib(n - 2)

def fib_with_cache(n, cache={0:0, 1:1}):
    # 停止遞迴的條件
    if n in cache: return cache[n]
    cache[n] = fib_with_cache(n - 1) + fib_with_cache(n - 2)
    return cache[n]

t1 = fib_performance(fib, 40)
t2 = fib_performance(fib_with_cache, 40)
print(f'fib 耗時 {t1} 奈秒')
print(f'fib_with_cache 耗時 {t2} 奈秒')