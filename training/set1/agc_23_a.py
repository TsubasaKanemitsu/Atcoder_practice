# https://www.youtube.com/watch?v=8BHBFMrZ8VM
# 解説AC

from collections import defaultdict
n = int(input())
A = list(map(int, input().split()))


# 考察1
# 1 <= N <= 2 * 10 ** 5より
# bit全探索による部分列の取り出し方の全探索はできない

# 考察2
# 連続する部分列の総和が0になればいい
# 尺取り法
# Aが単調増加関数ではないので、区間の総和が0という判定で個数を求めることができない


# 解法
# 累積和を取る
# 打ち消し合う組み合わせの数が幾つ？
# 2個以上同じものがあったらその組み合わせの数＝個数*(個数-1)//2を足す
cum_sum_a = [0]

for i in range(n):
    cum_sum_a.append(cum_sum_a[i] + A[i])
cnt = defaultdict(int)

for a in cum_sum_a:
    cnt[a] += 1

ans = 0
for k, v in cnt.items():
    ans += v * (v - 1) // 2
print(ans)