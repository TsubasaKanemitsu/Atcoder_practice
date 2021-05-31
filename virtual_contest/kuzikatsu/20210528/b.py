d, n = list(map(int, input().split()))

if d == 0:
    ans = n
    if ans // 100 == 1:
        ans = 101
elif d == 1:
    ans = 100 * n
    if ans == 100 ** 2:
        ans = 101 * n
else:
    ans = 100 ** 2 * n
    if ans == 100 ** 3:
        ans = 100 * 101 * n
print(ans)