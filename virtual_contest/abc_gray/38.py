# ABC 181C
# 5min
# 3点が同一直線状にあるかどうかを判定するだけ
# https://www.geisya.or.jp/~mwm48961/kou2/line_brief1.htm

n = int(input())

xy = []
for _ in range(n):
    x, y = list(map(int, input().split()))
    xy.append((x, y))

for i in range(n):
    x1, y1 = xy[i]
    for j in range(i + 1, n):
        x2, y2 = xy[j]
        for k in range(j + 1, n):
            x3, y3 = xy[k]

            if (y3 - y1) * (x2 - x1) == (y2 - y1) * (x3 - x1):
                print("Yes")
                exit()
print("No")