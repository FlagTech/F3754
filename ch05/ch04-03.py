year_str = input('請輸入生日的西元年份：')
if year_str.isdecimal(): # 只包含 10 進位數字
    year = int(year_str)
else:
    print('你輸入的不是數字。')  
    year = 2023 # 輸入錯誤時的預設值
print(f'你輸入的年份是：{year}')