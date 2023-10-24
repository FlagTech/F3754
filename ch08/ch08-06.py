registrations = {
    "小羚羊":("王一俊", "李二鈞", ),
    "勝利隊":("張小松", "吳俊廷", )
}

registrations['小羚羊'] = ('王一俊', '陳三維')
registrations['噴火龍'] = ("鄭時棋", "張俊欽", "陳四維", )
del registrations['勝利隊']

for team in registrations:
    print(f'{team}:')
    for member in registrations[team]:
        print(f'\t{member}')