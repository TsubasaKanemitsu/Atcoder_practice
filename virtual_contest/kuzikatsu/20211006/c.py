# 周期性問題
# TODO やり直し

n, k = list(map(int, input().split()))

A = list(map(int, input().split()))

visited = [1]
now = 1
for i in range(n):
    visited.append(A[now - 1])
    now = A[now - 1]
    if i == k - 1:
        print(now)
        exit()
num = visited[-1]
idx = visited.index(num)
periodic = len(visited) - 1 - idx
pos = idx + (k - idx) % periodic
ans = visited[pos]
print(ans)