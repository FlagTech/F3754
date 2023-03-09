def flower_book(flower):
    # 使用讀取模式開啟檔案
    with open('upload\\flower_book.txt', 'r', encoding='utf-8') as f: 
        flower_info = f.readlines()         # 逐行讀取並形成串列
    ans = ''                                # ans用來儲存花名與花語
    for i in flower_info:                   # 讀取花語串列
        book = i.split(',')                 # 用逗號切片花名與花語，因為資料是用逗號分隔
        if flower in book[0]:               # 如果輸入的花名有在花名資料其中
            ans += f"{book[0]}: {book[1]}\n"# 輸出完整花名與花語
    if len(ans) == 0:                       # 當ans沒有存入花語時
        ans = '查無此花語'
    return ans

if __name__ == "__main__":                  # 如果直接執行本檔案的主程式時
    flower = str(input('請輸入花名: '))      # 輸入花名
    print(flower_book(flower))              # 輸出函式回傳值(花語與花名)