from time import localtime

year_str = input('請輸入生日的西元年份：')
if year_str.isdecimal() and len(year_str) == 4:
    year = int(year_str)
else:
    year = localtime().tm_year
print(f'你出生在 {year} 年')