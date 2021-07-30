import sys
sys.setrecursionlimit(10 ** 7)
# 1 ~ 3の重複全探索
# 複雑な条件下における全探索を行うときにDFSを用いることがある。

# 全探索した値を保管するリストをグローバルに定義する
# 長さがN以下までは全探索を行う
# 場合によっては、探索を行わない条件を追加する

n = 3
global S
S = []

def dfs(num_list):
    print(num_list)
    if len(num_list) < n:
        for i in range(1, 4):
            dfs(num_list + [i])
    else:
        S.append(num_list)
        return


for i in range(1, 4):
    dfs([i])

print(S)