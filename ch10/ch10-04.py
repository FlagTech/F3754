def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

n = int(input('請輸入一個正整數：'))
print(f'{n}! = {factorial(n)}')