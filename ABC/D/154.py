n, k = list(map(int, input().split()))

p = list(map(int, input().split()))
cum_sum = [0]
for i in range(1, n + 1):
    cum_sum.append(cum_sum[i - 1] + (p[i - 1] + 1) / 2)
ans = 0
for i in range(n - k + 1):
    temp_ans = cum_sum[i + k] - cum_sum[i]
    ans = max(ans, temp_ans)
print(ans)

