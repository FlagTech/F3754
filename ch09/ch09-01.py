def input_4_diff_digits():
    while True:
        digits = input('請輸入 4 位不重複數字：')
        if not (digits.isdecimal() and len(digits) == 4):
            print('你輸入的不是 4 位數')
            continue

        for i in range(len(digits)):
            if digits[i] in digits[i + 1:]:
                print(f'{digits[i]} 重複了')
                break
        else:
            print(f'你輸入的是 {digits}')
            break

input_4_diff_digits()