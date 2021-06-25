import math
n = int(input())
A = list(map(int, input().split()))

ans = 0
i = 0
while i < n - 1:
    cnt = 0
    while A[i] == A[i + 1]:
        cnt += 1
        i += 1
        if i == n - 1:
            break
    ans += math.ceil(cnt / 2)
    i += 1
print(ans)
