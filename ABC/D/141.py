import heapq

n, m = list(map(int, input().split()))
A = list(map(int, input().split()))
A = list(map(lambda x: x * (-1), A))

heapq.heapify(A)

for i in range(m):
    min_val = heapq.heappop(A)
    half_val = (- min_val) // 2
    heapq.heappush(A, (-1) * half_val)
print(-sum(A))