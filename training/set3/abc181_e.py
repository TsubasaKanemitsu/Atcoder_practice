import bisect
# 解けなかった
# 復習 (重要)
# https://drken1215.hatenablog.com/entry/2020/11/02/021500

# 累積和、逆順累積和

# 身長差を最小化したいので、値が近い者同士の差を足し合わせるべきである
# => Hをソート
# => WがHの中で最も値の違い場所にあればいい => 二分探索で位置を探索
# => それぞれのWを最適な場所を選んで、差の総和を取り
# どのWの時が最も最小化できるのかを調べたい
# 差の総和を毎回とるとO(N^2)になってしまう(w毎に差の総和を調べる必要があるから)ので
# 差の取り方に計算の高速化が必要となる

n, m = list(map(int, input().split()))
H = list(map(int, input().split()))
W = list(map(int, input().split()))
H.sort()

diff = [H[i + 1] - H[i] for i in range(n - 1)]

# 左右からの累積和
# wの入る位置が左端や右端のとき
# 0を加算する必要があるので
# それぞれの端には0を追加している
left = [0] + diff[::2]
right = diff[1::2] + [0]

for i in range(len(left) - 1):
    left[i + 1] += left[i]
for i in range(len(right) - 1, 0, -1):
    right[i - 1] += right[i]

sum = 10 ** 18
for w in W:
    idx = bisect.bisect_left(H, w)
    if idx % 2 == 0:
        temp_sum = left[idx // 2] + right[idx // 2] + abs(w - H[idx])
    else:
        temp_sum = left[idx // 2] + right[idx // 2] + abs(w - H[idx - 1])
    sum = min(sum, temp_sum)
print(sum)