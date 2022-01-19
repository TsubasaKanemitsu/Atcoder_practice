import itertools
n, m = list(map(int, input().split()))

# 考察1
# 2 つのボールを 2 本以上の異なるひもが結んでいることはありません -> 多重グラフではない
# o=oみたいな状態にはならない

# 同一のボールを結ぶひもは存在しない -> 自己ループがない

# これらの性質より
# 閉路のない

T = [[False] * n for _ in range(n)]
A = [[False] * n for _ in range(n)]


for _ in range(m):
    a, b = list(map(int, input().split()))
    a -= 1
    b -= 1
    T[a][b] = True
    T[b][a] = True

for _ in range(m):
    c, d = list(map(int, input().split()))
    c -= 1
    d -= 1
    A[c][d] = True
    A[d][c] = True

for perm in itertools.permutations(range(n)):
    tree_same = True
    for i, pi in enumerate(perm):
        for j, pj in enumerate(perm):
            if T[i][j] != A[pi][pj]:
                tree_same = False
    if tree_same:
        print("Yes")
        exit()
print("No")
