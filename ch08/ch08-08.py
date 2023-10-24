registrations = {
    "小羚羊":["王一俊", "李二鈞"],
    "勝利隊":["張小松", "吳俊廷"]
}

for value in registrations.values():
    while(len(value) > 1):
        value.pop()

for key in registrations.keys():
    print(f'{key}: {registrations[key]}')