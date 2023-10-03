from time import localtime

year_str = input('請輸入生日的西元年份：')
if year_str.isdecimal(): # 只包含 10 進位數字
    year = int(year_str)
else:
    year = localtime().tm_year # 取得今年西元年份
print(f'你輸入的年份是：{year}')