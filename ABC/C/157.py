n, m = list(map(int, input().split()))

s = []
c = []

for i in range(m):
    _s, _c = list(input().split())
    s.append(int(_s))
    c.append(int(_c))
ans = ''
for i in range(1000):
    flag = True
    ans = str(i)

    if len(ans) != n:
        continue
    for j in range(m):
        # 同じ桁に対して別の数値の入力があった場合，無効になる
        if int(ans[s[j] - 1]) != c[j]:
            flag = False
    if flag:
        print(ans)
        exit(0)

print(-1)
    