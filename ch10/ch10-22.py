from pathlib import Path

def show_dir(path, level=0):
    print(f'{"  " * level}[{path.name}]')   # 先顯示資料夾名稱
    level += 1                 # 遞增層數
    dirs = [dir for dir in path.iterdir() if dir.is_dir()]
    dirs.sort()                # 排序資料夾名稱
    for dir in dirs:           # 先處理子資料夾
        show_dir(dir, level)   # 遞迴顯示子資料夾
    files = [file for file in path.iterdir() if file.is_file()]
    files.sort()             # 排序檔案名稱
    for file in files:      # 再處理檔案
        print(f'{"  " * level}{file.name}') # 向右縮排顯示檔名

def ls(path_str):
    path = Path(path_str)
    if not path.exists():      # 確認路徑是否存在？
        print('路徑不存在')
        return
    show_dir(path)

path_str = input('請輸入資料夾路徑：')
ls(path_str)