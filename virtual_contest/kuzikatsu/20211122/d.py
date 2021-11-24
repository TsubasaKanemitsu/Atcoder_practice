n, C = list(map(int, input().split()))

# iの範囲が小さければimos法が使えたが今回は使えない
# 座標圧縮 + imos法
# 1日に使うサービス料金がC円より高いときは、すぬけプライムに入る

# imos法を使うところと座標圧縮までは何とか思いついたが実装ができなかった。

event = list()
for i in range(n):
    a, b, c = list(map(int, input().split()))
    a -= 1
    event.append([a, c])
    event.append([b, -c])
event.sort()

ans = 0
fee = 0
# 前回のイベント
t = 0
for d, m in event:
    if d != t:
        ans += min(C, fee) * (d - t)
        t = d
    fee += m
print(ans)
