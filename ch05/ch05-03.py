from time import localtime
now = localtime()
print(f'{now.tm_year} 年 {now.tm_mon} 月 {now.tm_mday} 日')