# ABC 177 C
# 5min
# 累積和

N = int(input())
A = list(map(int, input().split()))

cum_sum_a = [A[0]]
for i in range(1, N):
    cum_sum_a.append(cum_sum_a[i - 1] + A[i])

ans = 0

for i in range(N):
    ans += A[i] * (cum_sum_a[N - 1] - cum_sum_a[i]) % (10 ** 9 + 7)
    # print(ans)
print(ans % (10 ** 9 + 7))