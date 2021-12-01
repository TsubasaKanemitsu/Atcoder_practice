n = int(input())

ans = 10 ** 9

for _ in range(n):
    a, p, x = list(map(int, input().split()))
    if x > a:
        ans = min(ans, p)
if ans == 10 ** 9:
    ans = -1
print(ans)