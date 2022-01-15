from collections import defaultdict
n, q = list(map(int, input().split()))
A = list(map(int, input().split()))

# Aiの出た回数と何番目なのか
# Ai, cnt[Ai] =  idx

cnt = defaultdict(int)

comb = defaultdict(int)

for i in range(n):
    cnt[A[i]] += 1
    comb[(A[i], cnt[A[i]])] = i + 1

ans = []
for i in range(q):
    x, k = list(map(int, input().split()))
    val = comb[(x, k)]
    if val == 0:
        val = -1
    ans.append(val)

for a in ans:
    print(a)