inf = 10 ** 20

N, M = list(map(int, input().split()))

# 全ての頂点の組についての最短距離を保存する2次元配列distを作る
dist = [[inf] * N for _ in range(N)]

# グラフの辺を受け取り、distに直接書き込む
for _ in range(M):
    u, v, c = list(map(int, input().split()))
    dist[u][v] = c

# iからiへの同じ頂点同士の距離は0としておく
for i in range(N):
    dist[i][i] = 0

# ワーシャル・フロイド法
for k in range(N):
    for x in range(N):
        for y in range(N):
            dist[x][y] = min(dist[x][y], dist[x][k] + dist[k][y])

ans = 0
for x in range(N):
    for y in range(N):
        ans += dist[x][y]
print(ans)