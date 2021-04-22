# 15分
# 累積和系の問題
n = int(input())
a = list(map(int, input().split()))
a.insert(0, 0)
a.append(0)

cum_sum = 0
for i in range(1, n + 2):
    cum_sum += abs(a[i] - a[i - 1])



for i in range(1, n + 1):
    ans = cum_sum - (abs(a[i - 1] - a[i]) + abs(a[i] - a[i + 1])) + abs(a[i - 1] - a[i + 1])
    print(ans)