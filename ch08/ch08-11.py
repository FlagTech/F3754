registrations = {
    "小羚羊":["王一俊", "李二鈞"],
    "勝利隊":["張小松", "吳俊廷"]
}

registrations.update({
    '噴火龍':['鄭時棋'],
    '小羚羊':["李二鈞"]
})
registrations.update([('自由車', ['吳宏至'])])
registrations.update(酷飛車隊=['洪宗彥'])

for team, members in registrations.items():
    print(team, members)