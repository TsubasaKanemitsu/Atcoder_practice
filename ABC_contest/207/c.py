n = int(input())
kukan = []
for i in range(n):
    t, l, r = list(map(int, input().split()))
    if t == 1:
        pass
    elif t == 2:
        r -= 0.5
        pass
    elif t == 3:
        l += 0.5
    elif t == 4:
        l += 0.5
        r -= 0.5
    kukan.append((l, r))
ans = 0
for i in range(n):
    l1, r1 = kukan[i]
    for j in range(i + 1, n):
        l2, r2 = kukan[j]
        if r1 < l2 or r2 < l1:
            pass
        else:
            ans += 1
        # print(l1, r1, l2, r2)
print(ans)