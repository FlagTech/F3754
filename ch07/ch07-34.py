import time
t = time.localtime()
print(t)
for i in t:
    print(i)
print(f'{t[3]}:{t[4]}:{t[5]}')
print(f'{t.tm_year}/{t.tm_mon}/{t.tm_mday}')