with open('台北天氣.csv', 'r', encoding='utf-8') as f:
    it = iter(f) # 取得走訪器
    while True:
        try:
            row = next(it) # 取得下一項資料
        except StopIteration:
            break
        print(row, end='')