# ABC 207 C
# 15min

n = int(input())

TLR = [list(map(int, input().split())) for _ in range(n)]
ans = 0
for i in range(n):
    t1, l1, r1 = TLR[i]
    if t1 == 2:
        r1 -= 0.5
    elif t1 == 3:
        l1 += 0.5
    elif t1 == 4:
        l1 += 0.5
        r1 -= 0.5

    for j in range(i + 1, n):
        t2, l2, r2 = TLR[j]
        
        if t2 == 2:
            r2 -= 0.5
        elif t2 == 3:
            l2 += 0.5
        elif t2 == 4:
            l2 += 0.5
            r2 -= 0.5
        
        if not (r1 < l2 or r2 < l1):
            ans += 1
print(ans)