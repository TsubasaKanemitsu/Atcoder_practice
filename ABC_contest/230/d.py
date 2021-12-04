# 区間スケジューリング
# 貪欲法


n, d = list(map(int, input().split()))
LR = [list(map(int, input().split())) for _ in range(n)]

LR.sort(key=lambda x:x[1])

# 区間Dを選んだときに、重なる壁の枚数が多いほどいい。
# 1. 各壁の位置毎に何枚の壁が存在しているのか知りたい
# -> Dは10 ** 9なのでimos法 + 座標圧縮で求められる
# 壁を壊したときに値の更新を行う必要がある

# 計算量無視 解法
# 各マスごとに重なっている壁の数を数える
# 区間Dをスライドさせていき、一番壁の枚数が多い区間を調べる
# 区間の位置が決まればパンチを実行する
# パンチされた壁の枚数分、重なっている壁を減らす

x = 0
ans = 0
for l, r in LR:
    if l > x:
        ans += 1
        x = r + d - 1
    else:
        pass
print(ans)
