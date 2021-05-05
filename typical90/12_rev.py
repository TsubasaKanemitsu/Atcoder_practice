# 復習必要
# 辺の連結はUnionFind木
# UnionFind木の主な処理は結合と集合

# 色が塗られているかを判定する配列を別に用意する
# queryが投げられるたびにその座標の周囲に赤で塗られているかどうかを確認する処理が必要
# 色が塗られている場合のみ，連結処理を行う．

# 間違えた点
# 赤色で塗られた箇所をBFSで探索してスタート地点から終了地点まで，
# 赤色で塗られている経路があれば，結合されていると判断しようとしていた．
# queryの個数だけで10 ** 5あるので，その中で毎回BFSで経路の探索をしていては
# 間に合わないことを計算量的に判断すべきだった．
# マス同士間で移動できるというのをマス同士が結合していると
# 言葉の言い換えをするべきだった．
# マス同士の移動 => マスの連結 => マス同士が同じグループに属する
# => マス同士の連結作業 and UnionFindで同じグループに属するか判定をさせる

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
    
    def issame(self, x, y):
        return self.find(x) == self.find(y)

    def size(self, x):
        return - 1 * self.parents[x]

    # def groups():
    #     out_dict = defaultdict(list)
    #     for i in range(self.n):
    #         parent = self.find(i)
    #         out_dict[parent].append(i)
    #     retu                    


h, w = list(map(int, input().split()))
Q = int(input())

used = [[False] * (w + 2) for _ in range(h + 2)]

uf = UnionFind(h * w)

# 結合
def query1(x, y):
    used[y][x] = True
    # 連結部分を探すために，周囲の4点が赤色で塗られているかを探索
    pos = ((0, 1), (0, -1), (1, 0), (-1, 0))
    for dx, dy in pos:
        px, py = x + dx, y + dy
        if not used[py][px]:
            continue
        hash_1 = w * (py - 1) + (px - 1)
        hash_2 = w * (y - 1) + (x - 1)
        uf.union(hash_1, hash_2)


def query2(ax, ay, bx, by):
    if not used[ay][ax] or not used[by][bx]:
        return False
    hash_1 = w * (ay - 1) + (ax - 1)
    hash_2 = w * (by - 1) + (bx - 1)
    ans = uf.issame(hash_1, hash_2)
    return ans


ans = []
for i in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 1:
        ri = q[1]
        ci = q[2]
        query1(ci, ri)
    else:
        rai = q[1]
        cai = q[2]
        rbi = q[3]
        cbi = q[4]
        answer = query2(cai, rai, cbi, rbi)
        if answer:
            ans.append("Yes")
        else:
            ans.append("No")
for a in ans:
    print(a)