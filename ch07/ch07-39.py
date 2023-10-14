board = (
    ['-', '-', '-'],
    ['-', '-', '-'],
    ['-', '-', '-']
)
turns = 0

while True:
    for row in board:
        for col in row:
            print(f'{col }', end=' ')
        print()
    print('-----------------')

    if turns == 9:
        print('平手')
        break

    row_str, col_str = input('請輸入座標：').split()
    if not row_str.isnumeric() or not col_str.isnumeric():
        print('請用空格輸入兩個數字')
        continue 
    row = int(row_str)
    col = int(col_str)
    if row < 0 or row > 2 or col < 0 or col > 2:
        print('請輸入 0~2 的數字')
        continue
    if board[row][col] != '-':
        print('此位置已有棋子')
        continue
    
    piece = 'O' if turns % 2 == 0 else 'X'
    board[row][col] = piece    
    turns += 1
        
    if (board[row].count(piece) == 3 
        or [r[col] for r in board].count(piece) == 3
        or [board[i][i] for i in range(3)].count(piece) == 3
        or [board[i][2-i] for i in range(3)].count(piece) == 3):
        print(f'{piece} 贏了')
        break