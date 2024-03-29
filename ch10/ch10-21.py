f = open('台北天氣.csv', 'r', encoding='utf-8')
f.readline() # 跳過第一行 (欄位名稱)
total = 0
rows_march = (row for row in f if '3月' in row)
temps = (float(row.split(',')[-1]) for row in rows_march)
for count, temp in enumerate(temps, start=1):
    total += temp
print(f'三月平均溫度：{total/count:.2f}')
f.close()