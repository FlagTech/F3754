# 從模組 (程式碼檔) 中匯入定義好的類別
import text_animator

class AdvTextAnimator(text_animator.TextAnimator):
    pass

heartbeat = AdvTextAnimator(
    r'·●⬤●·●⬤●·',
    0.3
)
heartbeat.run(3)   # 心跳的感覺