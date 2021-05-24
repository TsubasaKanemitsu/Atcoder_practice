# 領域加算は2次元いもす法
# 範囲に注意
# 1時間半

n = int(input())

lim = 10 ** 3 + 1

area = [[0] * lim for _ in range(lim)]

for _ in range(n):
    lx, ly, rx, ry = list(map(int, input().split()))
    # 左下
    area[ly][lx] += 1
    # 右下
    area[ly][rx] -= 1
    # 右上
    area[ry][rx] += 1
    # 左上
    area[ry][lx] -= 1


# x軸方向の累積和
for y in range(lim):
    temp = 0
    for x in range(1, lim):
        area[y][x] += area[y][x - 1]
        
# y軸方向の累積和
for x in range(lim):
    temp = 0
    for y in range(1, lim):
        area[y][x] += area[y - 1][x]
        
cnt = [0] * (10 ** 5 + 1)

for i in range(lim):
    for j in range(lim):
        num = area[i][j]
        cnt[num] += 1

for i in range(1, n + 1):
    print(cnt[i])