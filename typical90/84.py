n = int(input())
s = list(input())

ss = []

# ランレングス圧縮
i = 0
while i < n:
    now = s[i]
    cnt = 0
    while i < n and s[i] == now:
        cnt += 1
        i += 1
    if cnt != 0:
        ss.append((now, cnt))

comp = 0
for word, cnt in ss:
    comp += cnt * (cnt + 1) // 2

ans = n * (n + 1) // 2 - comp
print(ans)