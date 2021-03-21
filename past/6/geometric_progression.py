a, r, n = list(map(int, input().split()))

ans = a

if r == 1:
    print(a)
    exit()

# 大きい数字を扱うときは，少しずつ増やして
# 条件を超えるかを判定した方が良い
# 最初から大きい値は計算できない
for i in range(n - 1):
    ans *= r
    if ans > 10 ** 9:
        print('large')
        exit()
print(ans)