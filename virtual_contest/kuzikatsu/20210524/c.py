n = int(input())
a = list(map(int, input().split()))

cum_a = [a[0]]
inv_cum_a = [a[-1]]
for i in range(1, n):
    cum_a.append(cum_a[i - 1] + a[i])
    inv_cum_a.append(inv_cum_a[i - 1] + a[n - i - 1])

ans = 10 ** 99
for i in range(n - 1):
    diff = abs(cum_a[i] - inv_cum_a[n - i - 2])
    ans = min(ans, diff)
print(ans)