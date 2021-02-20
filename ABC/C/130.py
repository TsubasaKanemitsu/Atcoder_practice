# 考え方は惜しかった
w, h, x, y = list(map(int, input().split()))

s = w * h / 2
num = int(2 * x == w and 2 * y == h)
print(s, num)