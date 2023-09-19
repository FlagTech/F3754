bold =      "\x1B[1m"    # 粗體
normal =    "\x1B[0m"    # 預設
underline = "\x1B[4m"    # 底線
black =     "\x1B[30m"   # 黑色
red =       "\x1B[31m"   # 紅色
green =     "\x1B[32m"   # 綠色
yellow =    "\x1B[33m"   # 黃色
blue =      "\x1B[34m"   # 藍色
meganta =   "\x1B[35m"   # 洋紅
cyan =      "\x1B[36m"   # 青色
white =     "\x1B[37m"   # 白色
b_black =   "\x1B[40m"   # 以下設定背景
b_red =     "\x1B[41m"
b_green =   "\x1B[42m"
b_yellow =  "\x1B[43m"
b_blue =    "\x1B[44m"
b_meganta = "\x1B[45m"
b_cyan =    "\x1B[46m"
print(F"{normal}{black}Hello")
print(F"{bold}{red}Hello")
print(F"{normal}{underline}{green}Hello")
print(F"{normal}{blue}Hello")
print(F"{bold}{yellow}Hello")
print(F"{normal}{underline}{meganta}Hello")
print(F"{normal}{cyan}Hello")
print(F"{b_black}{white}Hello")
print(F"{b_red}Hello")
print(F"{b_green}Hello")
print(F"{b_blue}Hello")
print(F"{b_yellow}Hello")
print(F"{b_meganta}Hello")
print(F"{b_cyan}Hello")