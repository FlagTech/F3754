n_str = input('你想計算費式數列到第幾項？')
n = int(n_str)

f = {0:0, 1:1}

for curr in range(2, n + 1):
    f[curr] = f[curr - 1] + f[curr - 2]
    
print(f'費式數列到第 {n} 項如下：')
print(','.join([str(curr) for curr in f.values()]))