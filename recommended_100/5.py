a, b, c, x, y = list(map(int, input().split()))
pattern1 = 0
pattern2 = 0
pattern3 = 0

pattern1 = a * x + b * y
if x <= y:
    pattern2 = 2 * c * x + b * (y - x)
else:
    pattern2 = 2 * c * y + a * (x - y)
pattern3 = 2 * c * max(x, y)
print(min(pattern1, pattern2, pattern3))

# x, yの組み合わせの通りが10の10乗になるため，全探索で最少額を求めることができない
# そのため，計算量を減らすための工夫が必要
# A, Bをそれぞれの枚数ずつ購入する方法
# A, Bの最小値に合わせてABを購入し，AとBの差分については個別(A or B)で購入する方法
# A, Bの最大値に合わせて，全てをABで購入する方法