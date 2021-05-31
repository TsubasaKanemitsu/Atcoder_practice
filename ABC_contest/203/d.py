import math
N, K = list(map(int, input().split()))
A = [list(map(int, input().split())) for _ in range(N)]

all_median = [[0] * math.ceil(N / K) for _ in range(math.ceil(N / K))]
print(all_median)