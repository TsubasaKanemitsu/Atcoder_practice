from collections import defaultdict
n = int(input())
A = list(map(int, input().split()))

deta = set({A[0]})

cnt = defaultdict(int)
ans = 0

for i in range(n):
    ans += i - len(deta & set({A[i]})) * cnt[A[i]]
    cnt[A[i]] += 1
    deta.add(A[i])
print(ans)