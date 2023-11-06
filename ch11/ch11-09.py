try:
    f = open('config.txt', 'r+')
    try:
        name_old = f.readline().strip()
        name = input(f'你的名字 ({name_old})：')
        name = name or name_old
        f.seek(0)
        f.truncate()
        f.write(name)
    except KeyboardInterrupt:
        print('取消更新設定檔')
    f.close()
except FileNotFoundError as e:
    print(f'{e.filename} 設定檔不存在')