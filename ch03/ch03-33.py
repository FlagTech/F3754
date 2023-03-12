greeting = "hello, world"

# 正負索引可以混用
print(greeting[2:5])
print(greeting[-10:-7])
print(greeting[2:-7])
print(greeting[-10:5])
# 省略終點預設為字串長度
print(greeting[7:])
print(greeting[-5:])
# 省略起點預設為 0
print(greeting[:5])
print(greeting[:-7])
# 同時省略起點與終點
print(greeting[:])
# 起點在終點之後會取得空字串
print(greeting[2:1])
