from collections import defaultdict
n, m = list(map(int, input().split()))

s, c = [], []

for i in range(m):
    _s, _c = list(map(int, input().split()))
    s.append(_s)
    c.append(_c)

for i in range(1000):
    flag = True
    ans = str(i)
    if len(ans) != n:
        continue
    for j in range(m):
        if int(ans[s[j] - 1]) != c[j]:
            flag = False
    if flag:
        print(ans)
        exit()
print(-1)