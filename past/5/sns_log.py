# 復習
# グラフ問題は絵を書いてイメージをつかむ

from collections import defaultdict
n, q = list(map(int, input().split()))

f = [[False] * n for _ in range(n)]

for _ in range(q):
    s = input().split()
    if s[0] == '1':
        a = int(s[1]) - 1
        b = int(s[2]) - 1
        if a != b:
            f[a][b] = True
    elif s[0] == '2':
        a = int(s[1]) - 1
        for i in range(n):
            if f[i][a]:
                f[a][i] = True
    else:
        a = int(s[1]) - 1
        user = []
        for x in range(n):
            if f[a][x]:
                for j in range(n):
                    if f[x][j] and a != j:
                        # フォロー操作中にfの状態を書き換えると，
                        # 後の判定で結果がおかしくなる
                        # よって，一度別の場所に記録し，最後にTrueに置き換える
                        user.append(j)
        for u in list(set(user)):
            f[a][u] = True

for i in range(n):
    for j in range(n):
        if f[i][j]:
            print('Y', end='')
        else:
            print('N', end='')
    print()