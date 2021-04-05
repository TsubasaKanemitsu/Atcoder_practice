# 各Aiに対してAjが割り切れるかどうかを判定する配列と
# 与えられたAの数値の出現回数を保存する配列を用意する

# Aで2回以上同じ数値が出る数値は割り切れる数が存在することになるので
# 判定結果をFalseとすることで割り切れることを示す．

# AiをAjで割り切れるという考え方をAjの倍数のうち，Aiと同じになるものが
# 存在すると考え，Ajの倍数を全てFalseとしていく．
# 後で，Aに存在する数値の判定結果を見るだけなので，Aに存在しない部分にFalseが
# 入ることは特に問題はない．


from collections import defaultdict
n = int(input())
A = list(map(int, input().split()))

max_a = max(A)
cnt = defaultdict(int)

# Aに出現する数値の回数をカウントする
# 1以上であれば，aは割り切れることがわかる
for a in A:
    cnt[a] += 1

flag = [True] * (max_a + 1)

A = sorted(set(A))

for a in A:
    if cnt[a] > 1:
        flag[a] = False
    # Aの最大値までのaの約数が存在すれば, Falseにする
    # AiをAjで割り切れるという考え方から，Ajの倍数のうちAiとなるものを探す
    # という風に考え方を変える.
    for i in range(2 * a, max_a + 1, a):
        flag[i] = False

res = 0
for a in A:
    if flag[a]:
        res += 1
print(res)