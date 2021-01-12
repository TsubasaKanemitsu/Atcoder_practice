n, k = list(map(int, input().split()))

h = [int(input()) for _ in range(n)]
h.sort(reverse=True)
diff = 10 ** 9
for i in range(n - k + 1):
    temp_diff = h[i] - h[i + k - 1]
    diff = min(diff, temp_diff)

print(diff)