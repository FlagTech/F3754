f = open('台北天氣.csv', 'r', encoding='utf-8')
f.readline() # 跳過第一行 (欄位名稱)
temps = [float(row.split(',')[-1]) for row in f]
print(f'平均溫度：{sum(temps)/len(temps):.2f}')
f.close()