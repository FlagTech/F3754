up = '\x1B[1A'       # 游標上移一行
clear = '\x1B[2K'    # 清除游標所在行
green = '\x1B[32m'   # 綠色
blue = '\x1B[34m'    # 藍色
default = '\x1B[39m' # 預設色
tries = 5            # 最多猜 5 次

while True:
    q = input('請輸入 4 位不重複數字當謎題：')
    if not (q.isdecimal() and len(q) == 4):
        print('你輸入的不是 4 位數, 請重新輸入')
        continue

    for i in range(len(q)):
        if q[i] in q[i + 1:]:
            print(f'{q[i]} 重複了')
            break
    else:
        print(f'{up}{clear}\r已經輸入謎題, 進入猜謎遊戲')
        break

for _ in range(tries):
    A = B = 0
    ans = input('請猜猜看不重複的 4 位數字：')
    if not (ans.isdecimal() and len(ans) == 4):
        print('你輸入的不是 4 位數, 請重新輸入')
        continue

    for i in range(len(ans)):
        if ans[i] in ans[i + 1:]:
            print(f'{ans[i]} 重複了')
            break
    else:
        for i in range(len(ans)):
            if ans[i] == q[i]:
                A += 1
            elif ans[i] in q:
                B += 1
        if A == 4:
            print('你猜對了')
            break
        print(f'{green}{"Ⓐ "*A}{default}'
                f'{blue}{"Ⓑ "*B}{default}')
else:
    print(f'你沒有猜對, 答案是 {q}')