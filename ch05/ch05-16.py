year_str = input('請輸入生日的西元年份：')
year = int(year_str)

if year >= 2010:
    print(f'哇！你是生於 {year} 年手機世代的小孩耶！')
elif year >= 2000:
    print(f'你是生於 {year} 年網路世代的小孩')
elif year < 1990:
    print(f'不會吧？你是出生在 {year} 年的『前輩』！')