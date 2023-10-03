from time import localtime

year_str = input('請輸入生日的西元年份：')
if year_str.isdecimal(): # 只包含 10 進位數字
    year = int(year_str)
else:
    print('你輸入的不是數字。')
    year = localtime().tm_year # 取得今年西元年份
    # now = localtime()
    # year = now.tm_year
print(f'你輸入的年份是：{year}')