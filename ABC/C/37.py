n, k = list(map(int, input().split()))
A = list(map(int, input().split()))

ans = sum(A[:k])
kukanwa = ans

left = k
for i in range(n - k):
    j = i + k
    kukanwa = kukanwa + A[j] - A[i]
    ans += kukanwa
print(ans)


cum_sum_A = [A[0]]
for i in range(1, n):
    cum_sum_A.append(cum_sum_A[i - 1] + A[i])
cum_sum_A.insert(0, 0)
ans = 0
for i in range(len(cum_sum_A) - k):
    ans += cum_sum_A[i + k] - cum_sum_A[i]
print(ans)