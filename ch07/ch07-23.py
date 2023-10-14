board = [
    ['-', 'O', 'X'],
    ['X', 'O', 'X'],
    ['-', '-', 'O']
]    
board1 = board
board2 = board.copy()
print(board)
print(board1)
print(board2)
print('------------------')

board[2][0] = 'X'
print(board)
print(board1)
print(board2)
print('------------------')

board1[0][0] = 'O'
print(board)
print(board1)
print(board2)
print('------------------')

board2[2] = ['-', '-', '-']
print(board)
print(board1)
print(board2)
print('------------------')
