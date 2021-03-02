import bisect
n, m = list(map(int, input().split()))

h = list(map(int, input().split()))
w = list(map(int, input().split()))

h.sort()

# 要素が奇数の場合
# 差分の取り方は2パターン存在する
sum1 = [0] + [h[i + 1] - h[i] for i in range(0, n - 1, 2)]
sum2 = [h[i + 1] - h[i] for i in range(1, n - 1, 2)] + [0]

# 差分の累積和を取ることで，1つ値を挿入したときに，挿入箇所の差分と挿入箇所以外の差分を
# 瞬時に求めることができる．
for i in range(len(sum1) - 1):
    sum1[i + 1] += sum1[i]
for i in range(len(sum2) - 1, 0, -1):
    sum2[i - 1] += sum2[i]

ans = 1 << 60
for ww in w:
    x = bisect.bisect(h, ww)
    if x % 2 == 1:
        x -= 1
    cost = sum1[x // 2] + sum2[x // 2] + abs(h[x] - ww)
    if ans > cost:
        ans = cost
print(ans)