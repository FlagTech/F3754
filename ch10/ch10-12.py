import random
score = 0

def guess(n):
    a = int(input('猜 1~3 的數字：'))
    if n==a:
        score += 1 # 指派名稱會建立區域變數
        print(f'猜對 {n}')
    else:
        print(f'猜錯 {n}')

while True:
    n = random.randint(1, 3)
    guess(n)
    print(f'分數:{score}')
    if score == 3:
        print('遊戲結束')
        break