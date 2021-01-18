n = int(input())

A = list(map(int, input().split()))

sum_a = sum(A)

cum_sum = [A[0]]

for i in range(1, n):
    cum_sum.append(cum_sum[i - 1] + A[i])

diff = 10 ** 99
for i in range(n):
    temp_diff = abs(cum_sum[i] - (cum_sum[-1] - cum_sum[i]))
    diff = min(temp_diff, diff)
print(diff)