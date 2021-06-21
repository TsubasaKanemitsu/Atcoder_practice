from collections import defaultdict
n = int(input())
A = list(map(int, input().split()))

deta = set({A[0]})

cnt = defaultdict(int)
ans = 0

for i in range(n):
    ans += (i + 1) - len(deta & set({A[i]}) * cnt[A[i]]