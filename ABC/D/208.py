N, M = list(map(int, input().split()))

dist = [[10 ** 20] * N for _ in range(N)]

# 同じ頂点は距離0
for i in range(N):
    dist[i][i] = 0

for _ in range(M):
    a, b, c = list(map(int, input().split()))
    a -= 1
    b -= 1
    dist[a][b] = c

ans = 0
# 中継点を固定して、頂点間 x - y の最短経路をDP
# 今回の場合だと、K以下のパスを通るという条件下における
# 全てのパターンの最短経路にかかる時間を求める必要があるので
# Kのループが一番外にくる
for k in range(N):
    # 頂点がk以下までしか通れない状態での、頂点間 x - yでの最短経路
    for x in range(N):
        for y in range(N):
            dist[x][y] = min(dist[x][y], dist[x][k] + dist[k][y])
            # 道が存在していないところは通らない
            # k以下というのは、kを中継してxからyまで通る時間を全て足せばいい
            if not dist[x][y] == 10 ** 20:
                ans += dist[x][y]
print(ans)