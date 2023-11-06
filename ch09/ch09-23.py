up = '\x1B[1A'       # 游標上移一行
clear = '\x1B[2K'    # 清除游標所在行
green = '\x1B[32m'   # 綠色
blue = '\x1B[34m'    # 藍色
default = '\x1B[39m' # 預設色
tries = 5            # 最多猜 5 次

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

def scores(q, ans, /):
    A = B = 0
    for i in range(len(ans)):
        if ans[i] == q[i]:
            A += 1
        elif ans[i] in q:
            B += 1
    return A, B # 以序組傳回多個物件


# 以下是主程式
q = input_diff_digits('請輸入 4 位不重複數字當謎題：', 4)
print(f'{up}{clear}\r已經輸入謎題, 進入猜謎遊戲')

for _ in range(tries):
    ans = input_diff_digits('請猜猜看不重複的 4 位數字：', 4)
    # 使用多重指派取得計算的分數
    A, B = scores(q, ans)
    if A == 4:
        print('你猜對了')
        break
    print(f'{green}{"Ⓐ "*A}{default}'
          f'{blue}{"Ⓑ "*B}{default}')
else:
    print(f'你沒有猜對, 答案是 {q}')