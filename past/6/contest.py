n = int(input())
# 1始まりにするために先頭にダミーを入れる
ps = [0] + list(map(int, input().split()))

P = sum(ps)

# exist[i][s]: iまでの問題で合計をsにできる
exist = []
for i in range(n + 1):
    exist.append([False] * (P + 1))

# 初期条件
exist[0][0] = True

# iが小さい順にexistの値を求めていく
for i in range(1, n + 1):
    for s in range(P + 1):
        # 問題iを解かない場合
        if exist[i - 1][s]:
            exist[i][s] = True
        # 問題iを解く場合
        # 合計値以下かつps[i]を足したときにsになり得るために
        # i番目以前の選び方の中でs - ps[i] の値のなる状態があるかどうか
        if s >= ps[i] and exist[i - 1][s - ps[i]]:
            exist[i][s] = True
        
# 答えはexist[n][s]の中でTrueになっているsの個数
ans = 0
for s in range(P + 1):
    if exist[n][s]:
        ans += 1
print(ans)