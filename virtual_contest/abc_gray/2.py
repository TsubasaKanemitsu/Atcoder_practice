# 4分半
# 貪欲法

n, m = list(map(int, input().split()))

AB = [list(map(int, input().split())) for _ in range(n)]

AB.sort(key=lambda x:x[0])

ans = 0

for i in range(n):
    a, b = AB[i]
    m -= b
    if m >= 0:
        ans += a * b
    else:
        ans += a * (b + m)
        print(ans)
        exit()
print(ans)