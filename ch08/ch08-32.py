in_file = open('registrations.csv', 'r', encoding='utf')
out_file = open('backup.txt', 'w', encoding='utf')
for line in in_file:
    out_file.writelines([line])
in_file.close()
out_file.close()