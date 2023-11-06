import random
score = 0

while True:
    n = random.randint(1, 3)
    a = int(input('猜 1~3 的數字：'))
    if n==a:
        score += 1
        print(f'猜對 {n}')
    else:
        print(f'猜錯 {n}')
    print(f'分數:{score}')
    if score == 3:
        print('遊戲結束')
        break