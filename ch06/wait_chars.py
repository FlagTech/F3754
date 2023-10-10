import time

bars = r'―\|/―\|/'
circles_1 = '◑◒◐◓◑◒◐◓'
circles_2 = '·●⬤●·●⬤●·'
dots_1 = '⠹⠼⠶⠧⠏⠛⠹⠼⠶⠧⠏⠛'
dots_2 = '⠋⠙⠸⠴⠦⠇⠋⠙⠸⠴⠦⠇'
dots_3 = '⠁⠂⠄⠠⠐⠈⠁⠂⠄⠠⠐⠈'
blocks_1 = '▏▎▍▌▋▊▉▏▎▍▌▋▊▉'

print('\x1B[?25l', end='') # 隱藏游標
effects = [bars, circles_1, circles_2, dots_1, dots_2, dots_3, blocks_1]
for effect in effects:
    for char in effect:
        print(f'\r{char}', end='')
        time.sleep(0.3)
    time.sleep(1)
print('\x1B[?25h', end='') # 顯示游標