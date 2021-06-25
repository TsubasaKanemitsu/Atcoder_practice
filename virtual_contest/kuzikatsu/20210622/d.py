n = int(input())
A = list(map(int, input().split()))


class UnionFind:
    def __init__(self, n):
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        # 子頂点の場合，親の頂点をparentsに格納する
        else:
            # 経路圧縮
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return 0

        # xが常に親になるようにする
        if x > y:
            x, y = y, x
        self.parents[x] += self.parents[y]
        self.parents[y] = x


uf = UnionFind(2 * 10 ** 5)
for i in range(n // 2):
    if A[i] != A[n - i - 1]:
        uf.union(A[i] - 1, A[n - i - 1] - 1)

parents = uf.parents

ans = 0
for i in range(2 * 10 ** 5):
    if parents[i] < 0:
        ans += (- 1) * parents[i] - 1

print(ans)
