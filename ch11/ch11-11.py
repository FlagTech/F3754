try:
    config_file_name = input('設定檔名稱：')
    f = open(config_file_name, 'r+', encoding='utf-8')
    try:
        name_old = f.readline().strip()
        name = input(f'你的名字 ({name_old})：')
        name = name or name_old
        f.seek(0)
        f.truncate()
        f.write(name)
    except KeyboardInterrupt:
        print('取消更新設定檔')
    else:
        print('已成功更新設定檔')
    finally:
        f.close()
except FileNotFoundError as e:
    print(f'{e.filename} 設定檔不存在')