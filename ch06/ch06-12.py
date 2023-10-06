up = '\x1B[1A'       # 游標上移一行
clear = '\x1B[2K'    # 清除游標所在行
green = '\x1B[32m'   # 綠色
blue = '\x1B[34m'    # 藍色
default = '\x1B[39m' # 預設色
while True:
    q = input('請輸入 4 位不重複數字當謎題：')
    if not (q.isdecimal() and len(q) == 4):
        print('你輸入的不是 4 位數, 請重新輸入')
        continue

    curr = 0
    while curr < 3:
        if q[curr] in q[curr + 1:]:
            print(f'{q[curr]} 重複了')
            break
        curr += 1
    else:
        print(f'{up}{clear}\r已經輸入謎題, 進入猜謎遊戲')
        break

while True:
    A = B = 0
    ans = input('請猜猜看不重複的 4 位數字：')
    if not (ans.isdecimal() and len(ans) == 4):
        print('你輸入的不是 4 位數, 請重新輸入')
        continue

    curr = 0
    while curr < 3:
        if ans[curr] in ans[curr + 1:]:
            print(f'{ans[curr]} 重複了')
            break
        curr += 1
    else:
        curr = 0
        while curr < 4:
            if ans[curr] == q[curr]:
                A += 1
            elif ans[curr] in q:
                B += 1
            curr += 1
        if A == 4:
            print('你猜對了')
            break
        print(f'{green}{"Ⓐ "*A}{default}'
                f'{blue}{"Ⓑ "*B}{default}')