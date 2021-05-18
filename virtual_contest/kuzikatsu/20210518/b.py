from collections import deque
n = int(input())
S = list(input())

ans = deque(S[0])
for i in range(1, n):
    if ans[-1] != S[i]:
        ans.append(S[i])
print(len(ans))