year_str = input('請輸入生日的西元年份：')
if year_str.isdecimal(): # 只包含 10 進位數字
    year = int(year_str)
    print(f'你輸入的年份是：{year}')
else:
    print('你輸入的不是數字。')