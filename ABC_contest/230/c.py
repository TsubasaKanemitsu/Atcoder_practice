# 復習
# 不等号式の場合、言い換えに気を付ける
# 左端が0オフセットするように式変形を行う

n, a, b = list(map(int, input().split()))
p, q, r, s = list(map(int, input().split()))

# for i in range(p, q + 1):
#     for j in range(r, s + 1):
#         if i - j == a - b:
#             print("#", end="")
#         elif i + j == a + b:
#             print("#", end="")
#         else:
#             print(".", end="")
#     print()

mass = [['.'] * (s - r + 1) for i in range(q - p + 1)]


x = max(p - a, r - b)
y = min(q - a, s - b)
for i in range(x, y + 1):
    mass[a + i - p][b + i - r] = '#'

x = max(p - a, b - s)
y = min(q - a, b - r)
for i in range(x, y + 1):
    mass[a + i - p][b - i - r] = '#'

for m in mass:
    print(''.join(m))

