x1, y1, x2, y2 = list(map(float, input().split()))
distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
print(distance)

# 12分
# 小数点以下の計算をするときは，float型でキャストしておく