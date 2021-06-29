from collections import defaultdict, deque
n, m = list(map(int, input().split()))

path = defaultdict(list)

for _ in range(m):
    a, b = list(map(int, input().split()))
    path[a].append(b)
    path[b].append(a)


def bfs():
    Q = deque([1])
    
    visited = [False] * (n + 1)
    ans = [0] * (n + 1)
    visited[1] = True
    ans[1] = 1
    while len(Q) > 0:
        v = Q.popleft()
        for e in path[v]:
            if visited[e]:
                continue
            if ans[e] == 0:
                ans[e] = v
            visited[e] = True
            Q.append(e)
    return visited, ans


vis, ans = bfs()

if vis.count(True) == n:
    print("Yes")
    for i in range(2, n + 1):
        print(ans[i])
else:
    print("No")