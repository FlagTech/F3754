registrations = {
    ("小羚羊"):["王一俊", "李二鈞"],
    ("勝利隊"):["張小松", "吳俊廷"]
}

print(registrations.get(('小羚羊'), '查無此隊伍'))

registrations = {
    (["小羚羊"]):["王一俊", "李二鈞"],
    (["勝利隊"]):["張小松", "吳俊廷"]
}

print(registrations.get((["小羚羊"]), '查無此隊伍'))