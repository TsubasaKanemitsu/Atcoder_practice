# Ai - Ajが200の倍数になる組数を答える
# Ai - Ajが200の倍数になるとは，AiとAjを200で割ったあまりが一致するということ
# Aを200で割った値の各個数から組み合わせ数を求めればいい．

from collections import defaultdict
n = int(input())
A = list(map(int, input().split()))

cnt = defaultdict(int)

for i in range(n):
    cnt[A[i] % 200] += 1

ans = 0

for i in range(201):
    ans += cnt[i] * (cnt[i] - 1) // 2
print(ans)