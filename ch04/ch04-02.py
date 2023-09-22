principle = 1000000 # 本金
interest = 0.01     # 年息
years = 5           # 年數
msg = (f"本金 {principle} 經複利 {interest} 在 {years} 年後"
      + F"變成 {principle * (1 + interest) ** years}")
print(msg)
years += 5
print(msg)
