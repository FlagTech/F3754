f = open('conf.txt', 'r+', encoding='utf-8')
name_old = f.readline().strip()
name = input(f'你的名字 ({name_old})：')
name = name or name_old
f.seek(0)
f.truncate()
f.write(name)
f.close()