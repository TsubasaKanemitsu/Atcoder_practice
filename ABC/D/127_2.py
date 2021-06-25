from collections import Counter
n, m = list(map(int, input().split()))
A = list(map(int, input().split()))
A = list(Counter(A).items())
BC = []
for i in range(m):
    b, c = list(map(int, input().split()))
    BC.append((c, b))

A.extend(BC)
A.sort(key=lambda x:x[0], reverse=True)
ans = 0
cnt = 0
for i in range(len(A)):
    num, c = A[i]
    if cnt + c < n:
        ans += num * c
        cnt += c
    else:
        ans += num * (n - cnt)
        print(ans)
        exit()
