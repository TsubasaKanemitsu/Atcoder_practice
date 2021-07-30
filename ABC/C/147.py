# 復習
from collections import defaultdict
n = int(input())

# 人xから人yへの証言情報を格納
evidence = [[-1] * 15 for _ in range(15)]

for i in range(n):
    a = int(input())
    for j in range(a):
        x, y = list(map(int, input().split()))
        x -= 1
        # y = 0 or 1
        evidence[i][x] = y

cnt = 0
for bit in range(1 << n):
    honest = [0] * n
    for i in range(n):
        if bit & (1 << i):
            honest[i] = 1
    
    flag = True
    for i in range(n):
        # 証言に矛盾がないかチェック
        if honest[i]:
            for j in range(n):
                # 証言がない場合
                if evidence[i][j] == -1:
                    continue
                # 人iが人jを正直者か不親切かを証言しているので
                # その結果が人jは今回どちらで仮定して考えられている
                # パターンなのかを検証する
                if evidence[i][j] != honest[j]:
                    flag = False
    if flag:
        cnt = max(cnt, honest.count(1))
print(cnt)

# 学んだこと
# xからyを見たときの関係性を二次元配列で状態としてもつこと
