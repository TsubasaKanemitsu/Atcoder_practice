# 累積和の応用問題
# 復習
n = int(input())
a = list(map(int, input().split()))

ans = 0
a_cum = 0
all_cum = 0
max_val = 0

for i in range(n):
    a_cum += a[i]
    # i番目までの累積和で最大のもの
    # ex. a, a + b, a + b + cの中で最大となる数値を保持する
    max_val = max(max_val, a_cum)
    # i - 1番目までに進んだ距離とその距離から進みうるa, a + b, a + b + c, ...の中の最大の距離を足すことで
    # その段階における最大の距離を求められる
    # ここではi番目に行く過程の最大の距離を求めている
    ans = max(ans, all_cum + max_val)
    # i番目に進みきる距離に更新する
    all_cum += a_cum
print(ans)
