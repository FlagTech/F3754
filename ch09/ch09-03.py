def input_4_diff_digits(prompt):
    while True:
        digits = input(prompt) # 輸入 4 位數字
        if not (digits.isdecimal() and len(digits) == 4):
            print('你輸入的不是 4 位數')
            continue

        for i in range(len(digits)):
            if digits[i] in digits[i + 1:]:
                print(f'{digits[i]} 重複了')
                break
        else:
            return digits

q = input_4_diff_digits('請輸入 4 位不重複的數字當謎題：')
print(f'你輸入的謎題是 {q}')
a = input_4_diff_digits('請猜測 4 位不重複的數字：')
print(f'你猜測的是 {a}')