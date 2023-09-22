year_str = input('請輸入生日的西元年份：')
year = int(year_str) if year_str.isdecimal() else 2023
print(f'你輸入的年份是：{year}')