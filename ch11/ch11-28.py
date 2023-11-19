def update_config(filename):
    retry = True
    while True:
        try:
            with open(filename, 'r+', encoding='utf-8') as f:
                name_old = f.readline().strip()
                name = input(f'你的名字 ({name_old})：')
                name = name or name_old
                f.seek(0)
                f.truncate()
                f.write(name)
                break
        except FileNotFoundError:
            if not retry:
                print('預設設定檔不存在')
                raise FileNotFoundError(f'設定檔 {filename} 不存在')
            print(f'{filename} 設定檔不存在')
            filename = 'default.txt'
            retry = False

config_file_name = input('設定檔名稱：')
update_config(config_file_name)