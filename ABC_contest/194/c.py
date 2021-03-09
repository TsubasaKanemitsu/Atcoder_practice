n = int(input())
a = list(map(int, input().split()))
aa = a
a = a[::-1]
cum_sum = [a[0] ** 2]
cum_sum2 = [a[0]]
for i in range(1, n - 1):
    cum_sum.append(cum_sum[i - 1] + a[i] ** 2)
    cum_sum2.append(cum_sum2[i - 1] + a[i])
cum_sum = cum_sum[::-1]
cum_sum2 = cum_sum2[::-1] 
ans = 0
for i in range(len(cum_sum)):
    ans += cum_sum[i] - 2 * aa[i] * cum_sum2[i] + (n - 1 - i) * aa[i] ** 2
print(ans)