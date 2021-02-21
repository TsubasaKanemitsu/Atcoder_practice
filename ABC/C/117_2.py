# 9分
n = int(input())
a = list(map(int, input().split()))

rev_a = a[::-1]
cum_sum = [rev_a[0]]
for i in range(1, n - 1):
    cum_sum.append(cum_sum[i - 1] + rev_a[i])

cum_sum = cum_sum[::-1]
ans = 0

for i in range(n - 1):
    ans += a[i] * cum_sum[i]
print(ans % (10 ** 9 + 7))