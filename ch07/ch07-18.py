board = ['-', 'O', 'X']
print(f'棋盤現況：{board}')
board.append('-') # 在尾端新增 '-' 
print(f'棋盤現況：{board}')
board.extend(['O', 'X']) # 在尾端延伸 ['O', 'X']
print(f'棋盤現況：{board}')
board.insert(0, 'X') # 在索引 0 位置前插入 'X'
print(f'棋盤現況：{board}')
board.insert(len(board), '-') # 在尾端插入 '-'
print(f'棋盤現況：{board}')
board.remove('-') # 移除第 1 個 '-'
print(f'棋盤現況：{board}')
print(board.pop()) # 取出尾端項目
print(f'棋盤現況：{board}')
board.reverse() # 反轉
print(f'棋盤現況：{board}')
board.sort() # 排序
print(f'棋盤現況：{board}')
board.sort(reverse=True) # 排序
print(f'棋盤現況：{board}')
board1 = board.copy() # 複製
board.clear() # 清空
print(f'棋盤現況：{board}')
print(f'備份棋盤：{board1.copy()}')