registrations = (
    "小羚羊", ("王一俊", "李二鈞", ),
    "勝利隊", ("張小松", "吳俊廷", ),
    "飛飛卡丁車", ("許小陞", "劉大成", "張宏宇", ),
    "噴火龍", ("鄭時棋", "張俊欽", "陳四維", ),
    "自由車", ("吳宏至", "宋楚楚", "朱辰鈞", ),
    "酷飛車隊", ("洪宗彥", "簡孟均", "林是喬", ),
)

# 如果要查詢並顯示噴火龍隊的隊員
for index in range(0, len(registrations), 2):
    if registrations[index] == '噴火龍':
        for member in registrations[index + 1]:
            print(f'{member}')
        break