def not_n_digits(digits, n):
    if not (digits.isdecimal() and len(digits) == n):
        print(f'你輸入的不是 {n} 位數')
        return True
    return False

def digit_repeated(digits):
    for i in range(len(digits)):
        if digits[i] in digits[i + 1:]:
            print(f'{digits[i]} 重複了')
            return digits[i] # 傳回重複的數字
    return '' # 傳回空字串代表沒有重複的數字

def input_diff_digits(prompt, /, n, *, retry=-1, repeat=False):
    while retry != 0:
        retry -= 1 # 遞減嘗試次數
        # retry = max(-1, retry - 1) # 正確的寫法
        digits = input(prompt) # 輸入 4 位數字
        if not_n_digits(digits, n): # 如果不是 4 位數字
            continue # 重新輸入
        # 如果不允許數字重複, 但發現數字有重複
        if not repeat and digit_repeated(digits):
            continue # 重新輸入
        return digits
    print('超過次數, 放棄')
    return ''

q = input_diff_digits('給我 4 位不重複數字：', n=4, retry=1)
if q: print(f'你輸入的是 {q}')
q = input_diff_digits('給我 4 位不重複數字：', 4, 1)
if q: print(f'你輸入的是 {q}')