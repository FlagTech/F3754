board = ['-', 'O', 'X']
print(f'棋盤現況：{board}')
board[:2] = []
print(f'置換成空串列等於刪除切片：{board}')
board[:] = []
print(f'用切片清空串列：{board}')
board = ['-', 'O', 'X']
print(f'復原棋盤：{board}')
del board[:2] # 與 board[:2] = [] 相同
print(f'刪除前兩個項目：{board}')