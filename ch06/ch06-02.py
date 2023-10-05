done = False

while not done:
    q = input('請輸入 4 位數當謎題：')
    if not (q.isdecimal() and len(q) == 4):
        print('你輸入的不是 4 位數, 請重新輸入')
    else:
        done = True

print(f'你輸入的謎題是 {q}')