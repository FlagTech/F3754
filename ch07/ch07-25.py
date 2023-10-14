import copy

board = [
    ['-', 'O', 'X'],
    ['X', 'O', 'X'],
    ['-', '-', 'O']
]    
board1 = board
board2 = copy.copy(board)
board3 = copy.deepcopy(board)

print(f'board 的 id：{id(board)}')
print(f'board1 的 id：{id(board1)}')
print(f'board2 的 id：{id(board2)}')
print(f'board3 的 id：{id(board3)}')
print('------------------')

print(f'board == board1：{board == board1}')
print(f'board == board2：{board == board2}')
print(f'board == board3：{board == board3}')
print('------------------')

print(f'board is board1：{board is board1}')
print(f'board is board2：{board is board2}')
print(f'board is board3：{board is board3}')
print('------------------')