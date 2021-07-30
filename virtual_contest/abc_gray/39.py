# ABC 182C
# 3の倍数の性質(桁の和が3の倍数)
# bit全探索
n = list(map(int, list(input())))
nn = len(n)
ans = 10 ** 99
for bit in range(1 << nn):
    val = 0
    cnt = 0
    for i in range(nn):
        if bit & (1 << i):
            val += n[i]
            cnt += 1
    if val % 3 == 0 and nn - cnt != nn:
        ans = min(ans, nn - cnt)
if ans == 10 ** 99:
    print(-1)
    exit()
print(ans)