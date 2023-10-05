retry = 0
while retry < 3:
    q = input('請輸入 4 位數當謎題：')
    if q.isdecimal() and len(q) == 4:
        break
    else:
        print('你輸入的不是 4 位數, 請重新輸入')
    retry += 1
else:
    print(f'輸入 {retry} 次錯誤, 採用 1234 為預設謎題')
    q = '1234'

print(f'你輸入的謎題是 {q}')