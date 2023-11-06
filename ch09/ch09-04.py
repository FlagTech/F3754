def not_4_digits(digits):
    if not (digits.isdecimal() and len(digits) == 4):
        print('你輸入的不是 4 位數')
        return True
    return False

def digit_repeated(digits):
    for i in range(len(digits)):
        if digits[i] in digits[i + 1:]:
            print(f'{digits[i]} 重複了')
            return digits[i] # 傳回重複的數字
    return '' # 傳回空字串代表沒有重複的數字

def input_4_diff_digits(prompt):
    while True:
        digits = input(prompt) # 輸入 4 位數字
        if not_4_digits(digits): # 如果不是 4 位數字
            continue # 重新輸入

        if digit_repeated(digits): # 如果數字有重複
            continue # 重新輸入
        return digits

q = input_4_diff_digits('請輸入 4 位不重複的數字當謎題：')
print(f'你輸入的謎題是 {q}')
a = input_4_diff_digits('請猜測 4 位不重複的數字：')
print(f'你猜測的是 {a}')