from collections import defaultdict
n = int(input())
A = list(map(int, input().split()))

B = A.copy()
B.sort()
tr = defaultdict(int)
tr[B[0]] = 0
now = B[0]
cnt = 0
for i in range(n):
    if now < B[i]:
        cnt += 1
        tr[B[i]] = cnt
        now = B[i]
class UnionFind():
    def __init__(self, n):
        self.parents = [-1] * n
        # self.n = n

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

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def size(self, x):
        return - 1 * self.parents[x]

len = len(set(B))
uf = UnionFind(len)

cnt = 0
for i in range(n // 2):
    if A[i] == A[n - 1 - i]:
        continue
    if not uf.same(tr[A[i]], tr[A[n - 1 - i]]):
        cnt += 1
    uf.union(tr[A[i]], tr[A[n - 1 - i]])

par = uf.parents

ans = 0
for p in par:
    if p >= 0:
        continue
    p = abs(p)
    ans += p - 1
print(ans)