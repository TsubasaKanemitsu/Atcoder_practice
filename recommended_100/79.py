# 2次元累積和

n, m, q = list(map(int, input().split()))
cnt = [[0] * n for _ in range(n)]

for i in range(m):
    L, R = list(map(int, input().split()))
    L -= 1
    R -= 1
    cnt[L][R] += 1

for l in range(n):
    for r in range(1, n):
        cnt[l][r] += cnt[l][r - 1]

ans = []
for i in range(q):
    p, q = list(map(int, input().split()))
    p -= 1
    q -= 1
    res = 0
    for j in range(p, q + 1):
        res += cnt[j][q]
    ans.append(res)
for a in ans:
    print(a)