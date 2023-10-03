from time import localtime

year_str = input('請輸入西元年份：')
if year_str.isdecimal():
    year = int(year_str) 
else:
    year = localtime().tm_year 

if year % 4 != 0: # 規則 1
    # 西元年份不能被 4 整除者為平年, 不是潤年
    print(f"{year} 是平年")
else:
    if year % 100 != 0: # 規則 2
        # 西元年份可被 4 整除但不能被 100 整除者為潤年
        print(f'{year} 年是潤年')
    else:
        if year % 400 != 0: # 規則 3
            # 西元年份可被 100 整除但不能被 400 整除者為平年
            print(f'{year} 是平年')
        else: # 規則 4
            # 西元年份可被 400 整除者為潤年
            print(f"{year} 是潤年")
