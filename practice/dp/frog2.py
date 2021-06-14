n, k = list(map(int, input().split()))
h = list(map(int, input().split()))

cost = [0] * n

for i in range(1, n):
    cost[i] = cost[i - 1] + abs(h[i] - h[i - 1])
    j = 0
    while min(i, k) - j >= 0:
        cost[i] = min(cost[i], cost[i - j] + abs(h[i] - h[i - j]))
        j += 1
print(cost[-1])