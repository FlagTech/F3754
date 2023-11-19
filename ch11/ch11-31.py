def update_config(filename):
    assert filename, '檔名不可為空'
    with open(filename, 'r+', encoding='utf-8') as f:
        name_old = f.readline().strip()
        name = input(f'你的名字 ({name_old})：')
        name = name or name_old
        f.seek(0)
        f.truncate()
        f.write(name)

config_file_name = input('設定檔名稱：')
update_config(config_file_name)