n, C = list(map(int, input().split()))

event = []
for i in range(n):
    a, b, c = list(map(int, input().split()))
    a -= 1
    event.append((a, c))
    event.append((b, -c))

event.sort()
ans = 0
fee = 0
# 前回のイベント
t = 0
for x, y in event:
    if x != t:
        ans += min(C, fee) * (x - t)
        t = x
    fee += y
print(ans)
