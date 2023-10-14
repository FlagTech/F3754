import copy

board = [
    ['-', 'O', 'X'],
    ['X', 'O', 'X'],
    ['-', '-', 'O']
]    
board1 = copy.copy(board)
board2 = copy.deepcopy(board)
print(board)
print(board1)
print(board2)
print('------------------')

board[2][0] = 'X'
print(board)
print(board1)
print(board2)
print('------------------')