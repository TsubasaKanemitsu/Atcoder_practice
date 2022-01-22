# 方針はすぐについたがバグった
# 30分

n = int(input())
S = list(input())

# リーダの方向を向く
# i番目より左側にリーダーではない方向(西側)を向いている人数と
# i番目より右側にリーダーではない方向(東側)を向いている人数を知る必要がある
# i番目より左側と右側にそれぞれ、何人ずついるのかを知りたい
# 累積和でi番目までの人数を求めておけばいい。

# 東側を見なければならない人数
left = []
# 西側を見なければならない人数
right = []
cnt = 0
for i in range(n):
    left.append(cnt)
    if S[i] == 'W':
        cnt += 1

cnt = 0
for i in range(n - 1, -1, -1):
    right.append(cnt)
    if S[i] == 'E':
        cnt += 1
ans = 10 ** 9
for i in range(n):
    ans = min(ans, left[i] + right[n - i - 1])
print(ans)