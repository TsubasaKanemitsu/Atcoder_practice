n = int(input())
A = list(map(int, input().split()))
A.sort(reverse=True)

cum_sum_a = [A[0]]

for i in range(1, n):
    cum_sum_a.append(cum_sum_a[i - 1] + A[i])

ans = 0
for i in range(n - 1):
    ans += abs(cum_sum_a[i] - (i + 1) * A[i + 1])
    
print(ans)