from collections import Counter
n, k = list(map(int, input().split()))
a = list(map(int, input().split()))

hist = [0] * n
for i in a:
    hist[i] += 1

# print(hist)

ans = 0
val = [0] * n
# 0が存在する分だけ各箱は+1は確定するので
# 0の数の最小値と入れる箱の最小値の低い方の個数分+1される．
val[0] = min(k, hist[0])
ans += val[0]

for i in range(1, n):
    val[i] = min(k, val[i - 1], hist[i])
    # print(k, val[i - 1], hist[i])
    ans += val[i]

print(ans)