# 9分: 貪欲法
a, b, c, x, y = list(map(int, input().split()))

pattern1 = a * x + b * y
if x > y:
    pattern2 = (2 * c) * y + (x - y) * a
else:
    pattern2 = (2 * c) * x + (y - x) * b 
pattern3 = 2 * c * max(x, y)

print(min(pattern1, pattern2, pattern3))
