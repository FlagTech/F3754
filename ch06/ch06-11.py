while True:
    q = input('請輸入 4 位不重複數字當謎題：')
    if not (q.isdecimal() and len(q) == 4):
        print('你輸入的不是 4 位數, 請重新輸入')
        continue
    # 已確認輸入的是 4 位數字
    curr = 0
    while curr < 3:
        if q[curr] in q[curr + 1:]:
            print(f'{q[curr]} 重複了')
            break
        curr += 1
    else:
        print('已經輸入謎題, 進入猜謎遊戲')
        break