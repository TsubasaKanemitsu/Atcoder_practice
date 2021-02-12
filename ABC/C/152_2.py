# 10分
n = int(input())
p = list(map(int, input().split()))

cnt = 1
v = p[0]
# 最小値の更新
# 右側の数字が左側の数字より小さい個数分をカウントする
for j in range(1, n):
    if v > p[j]:
        v = p[j]
        cnt += 1
print(cnt)
