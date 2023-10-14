board = ['-', 'O', 'X']
print(f'棋盤現況：{board}')
board[0] = 'X'
print(f'下了叉後棋盤變成：{board}')
board[:2] = ['-', '-']
print(f'復原前兩個位置為未落子：{board}')
board_start = ['-', '-', '-']
board[2:] = board_start
print(f'延伸後棋盤：{board}')
board[::2] = ['X', 'O', 'X']
print(f'間隔置換後棋盤：{board}')