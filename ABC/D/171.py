from collections import Counter
from collections import defaultdict
n = int(input())
a = list(map(int, input().split()))
q = int(input())

sum_a = sum(a)
dict_a = defaultdict(int)
for i in a:
    dict_a[i] += 1
dp = []

for i in range(q):
    b, c = list(map(int, input().split()))
    num_b = dict_a[b]
    dict_a[c] += num_b
    dict_a[b] = 0
    sum_a += num_b * (c - b)
    dp.append(sum_a)

for i in range(q):
    print(dp[i])
