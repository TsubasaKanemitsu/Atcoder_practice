from collections import Counter
n, k = list(map(int, input().split()))
A = list(map(int, input().split()))

A = Counter(A)
A = sorted(A.items(), key=lambda x: x[1], reverse=True)

num_kind = len(A)
ans = 0
i = 0
while k < num_kind:
    ans += A[i][1]
    num_kind -= 1
    i += 1
print(ans)
