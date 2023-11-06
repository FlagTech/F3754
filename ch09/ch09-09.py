def scores(q, ans, /):
    A = B = 0
    for i in range(len(ans)):
        if ans[i] == q[i]:
            A += 1
        elif ans[i] in q:
            B += 1
    return A, B # 以序組傳回多個物件

# 使用多重指派取得傳回的分數
A, B = scores('1234', '1345')
print(f'{A}A{B}B')