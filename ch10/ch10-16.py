def temps(f):
    for row in f:
        yield float(row.split(',')[-1]) 

f = open('台北天氣.csv', 'r', encoding='utf-8')
f.readline() # 跳過第一行 (欄位名稱)
total = 0
for count, temp in enumerate(temps(f), start=1):
    total += temp
print(f'平均溫度：{total/count:.2f}')
f.close()