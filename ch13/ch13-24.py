import time
from threading import Timer
from adv_text_animator import AdvTextAnimator
import requests

def download_file(url):
    filename = None
    response = requests.get(url)
    if response.status_code == 200:
        if 'Content-Disposition' in response.headers:
            filename = (response.headers['Content-Disposition']
                    .split('=')[1])
        else:
            filename = url.split('/')[-1]
        with open(filename, "wb") as f:
            f.write(response.content)
    response.close()
    return filename

class ConcurrentTextAnimator(AdvTextAnimator):
    def start(self):
        interval = self.interval # 初始間隔時間
        idx = 0                  # 字元索引
        self.__timer = None      # 計時器
        def next_char():         # 顯示下一個字元
            nonlocal self, interval, idx
            print(f'\r{self.txt[idx]}', end='')
            idx = (idx + 1) % len(self.txt)
            if idx == 0:         # 一輪結束
                interval *= self.easing 
            self.__timer = Timer(interval, next_char)
            self.__timer.start() # 啟動計時器

        next_char()              # 開始動畫

    def stop(self):
        self.__timer.cancel()    # 停止計時器

bar_spinner = ConcurrentTextAnimator(
    r'―\|/―\|/',
    0.1,
    1     # 不變化速率
)

while True:
    url = input('請輸入要下載的檔案連結：')
    if url == '':
        break
    bar_spinner.start()
    filename = download_file(url)
    bar_spinner.stop()
    if filename:
        print(f'\n已下載 {filename}')
    else:
        print('無法下載檔案')