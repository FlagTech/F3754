try:
    f = open('conf.txt', 'r+', encoding='utf-8')
    name_old = f.readline().strip()
    name = input(f'你的名字 ({name_old})：')
    name = name or name_old
    f.seek(0)
    f.truncate()
    f.write(name)
    f.close() # 一切順利下關閉檔案
except FileNotFoundError as e:
    print(f'{e.filename} 設定檔不存在')
except KeyboardInterrupt:
    print('取消更新設定檔')
    f.close() # 輸入時強制中斷也要關閉檔案
# f.close() # 不能放這裡, 因為可能沒有成功開檔 