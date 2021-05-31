n, t = list(map(int, input().split()))

ans = 10 ** 10

for i in range(n):
    c, tt = list(map(int, input().split()))
    if tt <= t:
        ans = min(ans, c)
if ans == 10 ** 10:
    print("TLE")
    exit()
print(ans)