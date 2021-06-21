# 回文はある数字とある数字を1つにまとめる必要がある．
# 連結成分毎にまとめる(集合としてまとめていく => UnionFindが使えそう)
# 各連結成分を1つにまとめるには何回まとめる操作が必要になるのか?(=> 連結成分数 - 1)
# どういう時にまとめる作業が必要になるのか? => 回文になっていない，場所同士の数値

n = int(input())
A = list(map(int, input().split()))


class UnionFind():
    def __init__(self, n):
        self.parents = [-1] * n
    
    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        # x, yの頂点を探す
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return 0
        
        # 値が小さい方が親
        if self.parents[x] > self.parents[y]:
            x, y = y, x

        # 頂点x, yを結合する
        self.parents[x] += self.parents[y]
        self.parents[y] = x
        
        def size(self, x):
            return -1 * self.parents[x]


uf = UnionFind(2 * 10 ** 5 + 1)

for i in range(n // 2):
    if A[i] != A[n - i - 1]:
        uf.union(A[i] - 1, A[n - i - 1] - 1)

connected = uf.parents

ans = 0
for c in connected:
    if c < -1:
        ans += (-1 * c) - 1
print(ans)