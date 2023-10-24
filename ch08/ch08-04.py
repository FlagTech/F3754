registrations = {
    "小羚羊":("王一俊", "李二鈞", ),
    "勝利隊":("張小松", "吳俊廷", )
}

team_name = input('請輸入隊名：')
team = registrations[team_name]
for member in team:
    print(member)