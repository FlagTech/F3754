team_names= ("小羚羊", "勝利隊", "飛飛卡丁車", "噴火龍")
team_members= ("王一俊", "張小松", "許小陞")

registrations = dict(zip(team_names, team_members))

for team, member in registrations.items():
    print(team, member)