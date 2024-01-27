import time

def run_text(self, times):
    for _ in range(times):
        for ch in self.txt:
            print(f'\r{ch}', end='')
            time.sleep(self.interval)

class TextAnimator: # 定義名稱為 TextAnimator 的新類別
    pass

bar_spinner = TextAnimator()  # 建立一個 TextAnimator 實例
bar_spinner.txt = r'―\|/―\|/' # 增加屬性：動畫文字
bar_spinner.interval = 0.3    # 增加屬性：間隔時間
bar_spinner.run = run_text     # 增加屬性：動畫函式

bar_spinner.run(bar_spinner, 3)   # 執行動畫

heartbeat = TextAnimator()    # 建立一個 TextAnimator 實例
heartbeat.txt = '·●⬤●·●⬤●·' # 更換動畫文字
heartbeat.interval = 0.3    # 增加屬性：間隔時間
heartbeat.run = run_text     # 增加屬性：動畫函式

heartbeat.run(heartbeat, 3)   # 執行新動畫