n = int(input())

h = list(map(int, input().split()))

cost = [0] * n
cost[0] = 0
cost[1] = abs(h[0] - h[1])

for i in range(2, n):
    cost[i] = min(cost[i - 1] + abs(h[i] - h[i - 1]), cost[i - 2] + abs(h[i] - h[i - 2]))
print(cost[-1])