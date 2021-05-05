# 3分
# ハッシュテーブル
# データの存在有無の確認のO(1)を実現

n = int(input())
S = [input() for _ in range(n)]

resist_name = set()

ans = []
for i in range(n):
    if S[i] in resist_name:
        continue
    resist_name.add(S[i])
    print(i + 1)
