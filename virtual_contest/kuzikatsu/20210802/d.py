# 考察
# 境目より左にある黒石の数と右側にある白石の数の合計が最小になる
# 状態を求める
n = int(input())
x = list(input())

w = [0] * n
b = [0] * n

if x[0] == '.':
    w[0] = 1
else:
    b[0] = 1

for i in range(1, n):
    if x[i] == '.':
        w[i] = w[i - 1] + 1
        b[i] = b[i - 1]
    else:
        b[i] = b[i - 1] + 1
        w[i] = w[i - 1]
ans = 10 ** 6

for i in range(n):
    if x[i] == '#':
        ans = min(ans, b[i] - 1 + (w[n - 1] - w[i]))
    elif x[i] == '.':
        ans = min(ans, b[i] + (w[n - 1] - w[i]))

if ans == 10 ** 6:
    ans = 0
print(ans)
