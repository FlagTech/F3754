board = ['-', 'O', 'X']
print(f'board 有 {len(board)} 個項目')
print(f'board 開頭是：{board[1]}')
print(f'board[1:] 是：{board[1:]}')

print('board 的個別項目：')
for cell in board:
    print(cell)

board1 = board * 2
print(f'board 串接 2 次是 {board1}')
board3 = board + board1
print(f'board 串接 3 次是 {board3}')

print(f"'-' 在 board 中出現 {board.count('-')} 次") 
if 'X' in board:
    print(f"'X' 出現在索引位置：{board.index('X')}")