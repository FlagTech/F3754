import time

def text_animation(self, repeat):
    for _ in range(repeat):
        for ch in self['text']:
            print(f'\r{ch}', end='')
            time.sleep(self['interval'])

# 用字典把要傳入的引數與函式包裝起來
bar_animation = {
    'text': r'―\|/―\|/',  # 動畫文字
    'interval': 0.3,      # 間隔時間
    'run': text_animation # 執行函式
}

circle_animation = {
    'text': r'◑◒◐◓◑◒◐◓',  # 動畫文字
    'interval': 0.3,      # 間隔時間
    'run': text_animation # 執行函式
}

# 呼叫時別忘了把字典自己傳進去
bar_animation['run'](bar_animation, 3)
circle_animation['run'](circle_animation, 3)
