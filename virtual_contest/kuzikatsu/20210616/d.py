import heapq
# heapqは最小値(最大値)をO(logN)で取り出すことができる

n, m = list(map(int, input().split()))

A = list(map(int, input().split()))
A = list(map(lambda x: - x, A))

heapq.heapify(A)

ans = 0
for i in range(m):
    product = heapq.heappop(A)
    product *= -1
    product = product // 2
    product *= -1
    heapq.heappush(A, product)

print(-sum(A))