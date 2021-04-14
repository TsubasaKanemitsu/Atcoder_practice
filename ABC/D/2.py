n, m = list(map(int, input().split()))
xy = [list(map(int, input().split())) for _ in range(m)]

ans = 0
for bit in range(1 << m):
    selected = []
    for i in range(m):
        # 選ばれた議員の組み合わせ
        if bit & 1 << i:
            x = xy[i][0]
            y = xy[i][1]
            selected.extend([x, y])
    selected = sorted(list(set(selected)))
    comb = []
    for i in range(len(selected)):
        for j in range(i + 1, len(selected)):
            a = selected[i]
            b = selected[j]
            comb.append([a, b])
    cnt = 0
    for i in range(len(comb)):
        flag = False
        for j in range(m):
            a, b = comb[i]
            x, y = xy[j]
            if a == x and b == y:
                cnt += 1
    if cnt == len(comb):
        val = set()
        for a, b in comb:
            val.add(a)
            val.add(b)
        ans = max(ans, len(val))

print(ans)