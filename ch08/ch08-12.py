registrations = {
    "小羚羊":["王一俊", "李二鈞"],
    "勝利隊":["張小松", "吳俊廷"]
}

registrations1 = {
    '噴火龍':['鄭時棋'],
    '小羚羊':["李二鈞"]
}

new_registrations = registrations | registrations1

for team, members in new_registrations.items():
    print(team, members)
print('-' * 20)

registrations.update([('小羚羊', ['王一俊'])])

for team, members in registrations.items():
    print(team, members)
print('-' * 20)

for team, members in new_registrations.items():
    print(team, members)
print('-' * 20)

registrations1['噴火龍'].append('陳四維')

for team, members in new_registrations.items():
    print(team, members)