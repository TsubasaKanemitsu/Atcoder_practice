# 復習
from collections import defaultdict
n, m = list(map(int, input().split()))

class UnionFind():
    def __init__(self, n):
        self.parents = [-1] * n
    
    # 親を見つける
    def find(self, x):
        # 頂点の場合
        if self.parents[x] < 0:
            return x
        # 子頂点の場合，親の頂点をparentsに格納する
        else:
            # 経路圧縮
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]
    
    def union(self, x, y):
        # x, yの頂点を探す
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return 0

        # xの頂点がyの頂点より大きい場合, 入れ替える        
        if self.parents[x] > self.parents[y]:
            x, y = y, x

        # 頂点x, yを結合する
        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return - 1 * self.parents[x]


uf = UnionFind(n)
for i in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    uf.union(a, b)

ans = 0
for i in range(n):
    ans = max(ans, uf.size(i))
print(ans)

