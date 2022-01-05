import sys
sys.setrecursionlimit(10 ** 7)
from collections import defaultdict
n, m = list(map(int, input().split()))

if m == 0:
    print("Yes")
    exit()

G = defaultdict(list)


class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

    def __str__(self):
        return '\n'.join(f'{r}: {m}' for r, m in self.all_group_members().items())

dist = [-1] * n
def dfs(v, d):
    if dist[v] >= 0:
        return
    
    dist[v] = d
    for e in G[v]:
        dfs(e, d + 1)

# 並びの左端と右端は一番小さい、一番大きい番号が端になるので、
# そこから始めたときに、1本の木構造になっているかを探索すればいい


uf = UnionFind(n)
for _ in range(m):
    a, b = list(map(int, input().split()))
    a, b = a - 1, b - 1
    G[a].append(b)
    G[b].append(a)
    if uf.find(a) == uf.find(b):
        print("No")
        exit()
    uf.union(a, b)

# グループの数
# グループの根を探索
# 各根のメンバーを見る
# メンバ数が

root = uf.roots()
for r in root:
    size = uf.size(r)
    if size == 1:
        continue
    dist = [-1] * n
    dfs(r, 0)
    if max(dist) != size - 1:
        print("No")
        exit()
print("Yes")