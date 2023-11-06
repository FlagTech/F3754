def update_config(filename):
    f = open(filename, 'r+', encoding='utf-8')
    try:
        name_old = f.readline().strip()
        name = input(f'你的名字 ({name_old})：')
        name = name or name_old
        f.seek(0)
        f.truncate()
        f.write(name)
    finally:
        f.close()
try:
    update_config('conf.txt')
except OSError as e:
    print('設定檔可能被移除了')
except FileNotFoundError as e:
    print(f'{e.filename} 設定檔不存在')
except KeyboardInterrupt:
    print('取消更新設定檔')
except:
    print('發生未知錯誤')
else:
    print('已成功更新設定檔')