import bisect
n, q = list(map(int, input().split()))

A = [0] + list(map(int, input().split()))
diff_a = [A[i + 1] - A[i] - 1 for i in range(n)]
cum_sum = [diff_a[0]]

# Ai以下の良い整数の個数を記録
for i in range(1, len(diff_a)):
	cum_sum.append(cum_sum[i - 1] + diff_a[i])

ans = []
for i in range(q):
	k = int(input())
	index = bisect.bisect_left(cum_sum, k)
	ans.append(index + k)

for a in ans:
	print(a)