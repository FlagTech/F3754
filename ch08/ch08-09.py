registrations = {
    "小羚羊":["王一俊", "李二鈞"],
    "勝利隊":["張小松", "吳俊廷"]
}

print(registrations.get('噴火龍', '查無此隊伍'))
print(registrations.setdefault('噴火龍', ["鄭時棋"]))
print(registrations.get('噴火龍', '查無此隊伍'))