from collections import deque
R, C = list(map(int, input().split()))
sy, sx = list(map(int, input().split()))
gy, gx = list(map(int, input().split()))
c = [list(input()) for _ in range(R)]

n = R * C
visited = [[False] * C for _ in range(R)]

sy -= 1
sx -= 1
gy -= 1
gx -= 1

# 始点からの最小移動回数を管理する2次元配列．-1であれば，未訪問であることを表す
# 移動回数の定義
# ある地点におけるスタート地点からの距離
dist = []
for i in range(R):
    dist.append([-1] * C)

Q = deque()
Q.append([sy, sx])
visited[sy][sx] = True


# キューの中身がなくなるまで
while len(Q) > 0:
    i, j = Q.popleft()
    # 4方向の確認 & 経路探索
    for y, x in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
        # 範囲外
        if not(0 <= y < R and 0 <= x < C):
            continue
        # 壁の場合
        if c[y][x] == '#':
            continue
        # 未訪問であれば距離を更新してキューに入れる
        if dist[y][x] == -1:
            # 前回までのスタート地点からの距離から+1する
            dist[y][x] = dist[i][j] + 1
            Q.append([y, x])
print(dist[gy][gx] + 1)
