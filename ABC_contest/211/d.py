from collections import defaultdict, deque
n, m = list(map(int, input().split()))

graph = defaultdict(list)
for _ in range(m):
    x, y = list(map(int, input().split()))
    graph[x].append(y)
    graph[y].append(x)


def bfs():
    Q = deque()
    Q.append(1)
    
    visited = [False] * (n + 1)
    dist = [0] * (n + 1)
    cnt = [0] * (n + 1)

    visited[1] = True
    cnt[1] = 1

    while len(Q) > 0:
        v = Q.popleft()
        for e in graph[v]:
            # 未到達の場合
            if not visited[e]:
                dist[e] = dist[v] + 1
                visited[e] = True
                Q.append(e)
                cnt[e] = cnt[v]
            
            # 到達済みかつ最短距離の場合
            # 通り数を加算する
            elif dist[e] == dist[v] + 1:
                cnt[e] += cnt[v]
                cnt[e] %= (10 ** 9 + 7)
                
    return cnt[n]


ans = bfs()

print(ans)
