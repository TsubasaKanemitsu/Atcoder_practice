n, w = list(map(int, input().split()))

AB = [list(map(int, input().split())) for _ in range(n)]

AB.sort(reverse=True, key=lambda x:x[0])
ans = 0
for a, b in AB:
    if w - b >= 0:
        ans += a * b
        w -= b
    else:
        ans += w * a
        break
print(ans)

