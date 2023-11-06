def fib_with_cache(n, cache={0:0, 1:1}):
    # 停止遞迴的條件
    if n in cache: return cache[n]
    cache[n] = fib_with_cache(n - 1) + fib_with_cache(n - 2)
    return cache[n]

for i in range(40):
    print(f'{i}:{fib_with_cache(i)}')