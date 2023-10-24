in_file = open('registrations.csv', 'r', encoding='utf')
out_file = open('backup.txt', 'w', encoding='utf')
registrations = {}
for line in in_file:
    team, member = line.split()
    registrations.setdefault(team, []).append(member)
for team, members in registrations.items():
    print(team, ', '.join(members), file=out_file)
in_file.close()
out_file.close()