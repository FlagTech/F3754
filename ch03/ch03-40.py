print("1A中二".isalnum())   # 中文字元也是字母
print("1,A中".isalnum())  # "," 是標點符號, 不是字母
print("123".isalpha())    # 這是數字、不是字母
print("123".isascii())    # ASCII 編碼範圍
print("123".isdecimal())  # 10 進位數字
print("hello".islower())  # 小寫字母
print("12三四壹".isnumeric()) # 中文數字算在數字類
print("\n \t\r".isspace()) # 換行、歸位等都算空白
print("HELLO".isupper())  # 大寫字母
