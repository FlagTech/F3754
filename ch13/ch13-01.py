# 從模組 (程式碼檔) 中匯入定義好的類別
import text_animator

heartbeat = text_animator.TextAnimator(
    r'·●⬤●·●⬤●·',
    0.3
)
heartbeat.run(3)   # 心跳的感覺