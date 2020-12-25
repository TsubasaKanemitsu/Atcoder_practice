n = int(input())
A = list(map(int, input().split()))
cum_sum = [sum(A[1:])]
for i in range(n - 2):
    cum_sum.append(cum_sum[i] - A[i + 1])

ans = 0
for i in range(n - 1):
    ans += A[i] * cum_sum[i]

print(ans % (10 **9 + 7))