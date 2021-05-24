n = int(input())
A = list(map(int, input().split()))

cum_a = [A[0]]
for i in range(1, n):
    cum_a.append(cum_a[i - 1] + A[i])
cum_a.insert(0, 0)
ans = [0] * (n + 1)

for i in range(n + 1):
    for j in range(i, n + 1):
        if i != j:
            ans[j - i] = max(ans[j - i], cum_a[j] - cum_a[i])

for i in range(1, n + 1):
    print(ans[i])