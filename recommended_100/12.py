# 復習
# 最大クリーク問題
n, m = list(map(int, input().split()))
XY = [list(map(int, input().split())) for _ in range(m)]

ans = 1
for bit in range(1 << n):
    selected = []
    for i in range(n):
        if bit & (1 << i):
            selected.append(i + 1)
    cnt = 0
    jk_cnt = 0
    member = set()
    for j in range(len(selected)):
        for k in range(j + 1, len(selected)):
            jk_cnt += 1
            for x, y in XY:
                if selected[j] == x and selected[k] == y:
                    cnt += 1
                    member.add(x)
                    member.add(y)
                    break
    if cnt == jk_cnt:
        ans = max(ans, len(member))

print(ans)