N, m, t = list(map(int, input().split()))
AB = [list(map(int, input().split())) for _ in range(m)]

n = N
last_time = 0
for i in range(m):
    a, b = AB[i]
    n -= a - last_time
    if n <= 0:
        print("No")
        exit()
    n += (b - a)
    n = min(N, n)
    last_time = b

n -= t - last_time
if n <= 0:
    print("No")
else:
    print("Yes")