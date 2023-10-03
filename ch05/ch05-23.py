from time import localtime

year_str = input('請輸入生日的西元年份：')
if not year_str.isdecimal() or not len(year_str) == 4:
    year = localtime().tm_year
else:
    year = int(year_str)
print(f'你出生在 {year} 年')