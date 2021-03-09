from collections import deque

# 長点数 N, 辺情報 E, 始点 sは定義済みとする

# 探索済みの頂点を管理する
visited = []
for i in range(n):
    visited.append(False)

# 始点は探索済みであることを記述している
Q = deque()
Q.append(s)
visited[s] = True

while len(Q) > 0:
    # キューの先頭を取り出す
    # 探索済みの頂点
    i = Q.popleft()
    # E[i]に含まれる頂点情報を列挙
    for j in E[i]:
        # 訪問していない場合，探索対象として追加する
        if not visited[j]:
            visited[j] = True
            Q.append(j)