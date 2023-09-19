principle = 1_000_000 # 本金
interest =  0.03      # 年息
years = int(input("請輸入年數："))            # 年數
total = principle * (1 + interest) ** years # 本金加利息
print(f"本金 {principle} 經複利 {interest} 在 {years} 年後"
      + F"變成 {total:15.2f}")
