n = int(input())
x = list(map(int, input().split()))

min_hp = 10000 ** 2
for p in range(max(x) + 1):
    hp = 0
    for j in x:
        hp += (j - p) ** 2
    min_hp = min(min_hp, hp)

print(min_hp)

# 1重目のループは最大値は，住人の座標のうちの最大値と考えた．
# その理由は，x[i] - pとした場合，x[i]のうちの最大値以上の座標を選んでも
# 住人からの距離が離れるだけで体力消費の最小値とはならないのは当然だから．