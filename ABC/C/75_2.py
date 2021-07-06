class UnionFind():
    def __init__(self, n):
        self.parents = [-1] * n

    def find(self, x):
        # 頂点の場合
        if self.parents[x] < 0:
            return x
        # 子頂点の場合、親の頂点をparentsに格納する
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        # x, yの頂点を探す
        x = self.find(x)
        y = self.find(y)

        # 頂点が同じ場合
        if x == y:
            return
        
        # 頂点が異なる状態で
        # yの集合の木が大きいとき
        if self.parents[x] > self.parents[y]:
            x, y = y, x
            # yの親をxの親に変更する
            
        self.parents[x] += self.parents[y]
        self.parents[y] = x


N, M = list(map(int, input().split()))
AB = [list(map(int, input().split())) for _ in range(M)]

bridge = 0
for i in range(M):
    uf = UnionFind(N)
    for j in range(M):
        if i == j:
            continue
        a, b = AB[j]
        a -= 1
        b -= 1
        uf.union(a, b)

    # 頂点の状態がどのようになっているかを確認する
    if -1 * min(uf.parents) != N:
        bridge += 1
print(bridge)