board = (
    ['X', 'O', 'O'],
    ['X', 'X', 'O'],
    ['-', 'X', 'O']
)

for col in range(3):
    if [row[col] for row in board].count('O') == 3:
        print(f'第 {col} 直行連成一線！')
        break