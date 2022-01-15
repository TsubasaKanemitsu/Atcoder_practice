# 復習
from collections import defaultdict, deque

n, m = list(map(int, input().split()))
graph = defaultdict(list)
dp = defaultdict(int)
for _ in range(m):
    a, b = list(map(int, input().split()))
    a -= 1
    b -= 1
    graph[a].append(b)
    graph[b].append(a)



def bfs():

    visited = [False] * n
    dist = [0] * n
    cnt = [0] * n
    cnt[0] = 1
    visited[0] = True


    Q = deque()
    Q.append(0)

    while len(Q) > 0:
        v = Q.popleft()
        for e in graph[v]:
            if not visited[e]:
                dist[e] = dist[v] + 1
                visited[e] = True
                Q.append(e)
                cnt[e] = cnt[v]

            elif dist[e] == dist[v] + 1:
                cnt[e] += cnt[v]
                cnt[e] %= (10 ** 9 + 7)

    return cnt[n - 1]

ans = bfs()
print(ans)