# 可讓使用者輸入半徑再計算圓周長與圓面積的範例
radius_string = input('請輸入半徑：') # 取得使用者輸入的半徑
radius = int(radius_string)           # 依據字串內容產生整數
pi = 3.14159                          # 圓周率
print('圓周長：', 2 * pi * radius)    # 計算並顯示圓周長
print('圓面積：', pi * (radius ** 2)) # 計算並顯示圓面積
