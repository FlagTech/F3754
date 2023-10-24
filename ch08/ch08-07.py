registrations = {
    "小羚羊":("王一俊", "李二鈞", ),
    "勝利隊":("張小松", "吳俊廷", )
}

keys = registrations.keys()
for key in keys:
    print(key)

for value in registrations.values():
    print(value)

for key, value in registrations.items():
    print(f'{key}: {value}')

registrations.clear()
print(f'鍵的數量：{len(keys)}')