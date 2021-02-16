from collections import defaultdict
h, w = list(map(int, input().split()))
n = int(input())
a = list(map(int, input().split()))

mass = [0 for _ in range(w) for _ in range(h)]

cnt = 0
for i in range(n):
    for j in range(cnt, cnt + a[i]):
        mass[j] = i + 1
    cnt += a[i]

ans = [[0 for _ in range(w)] for _ in range(h)]
cnt = 0
for i in range(h):
    for j in range(w):
        ans[i][j] = mass[cnt]
        cnt += 1

for i in range(h):
    if i % 2 == 1:
        ans[i].reverse()
    for j in range(w):
        print(ans[i][j], end=" ")
    print()
