from collections import deque
a, n = list(map(int, input().split()))

M = 1
while M <= n:
    M *= 10

def bfs():
    Q = deque()
    visited = [False] * M

    dist = [0] * M
    visited[1] = True

    Q.append(1)

    while len(Q) > 0:
        v = Q.popleft()

        if v * a < M and not visited[v * a]:
            visited[v * a] = True
            dist[v * a] = dist[v] + 1
            Q.append(v * a)

        if v >= 10 and v % 10 != 0:
            vv = int(str(v)[-1] + str(v)[0:-1])
            if vv < M and not visited[vv]:
                visited[vv] = True
                dist[vv] = dist[v] + 1
                Q.append(vv)
    return dist


dist = bfs()
if dist[n] == 0:
    print(-1)
else:
    print(dist[n])