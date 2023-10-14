board = ['-', 'O', 'X']
print(f'棋盤現況：{board}')
board[:2] = ('X', '-')
print(f'用序列置換前兩個項目：{board}')

numbers = []
numbers[:] = range(5)
print(f'numbers = {numbers}')