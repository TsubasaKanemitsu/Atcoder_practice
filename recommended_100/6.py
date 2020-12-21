n = int(input())
s = input()
l = [str(i) for i in range(10)]
from itertools import product
ans = 0

for i in product(l, repeat=3):
    j = 0
    for w in s:
        if w == i[j]:
            j += 1
        if j == 3:
            ans += 1
            break
print(ans)

# Sの部分列であるかを判定する問題
# 3桁の暗証番号になりえるのは, 0~9, 0~9, 0~9の10の3乗通り存在する(文字列tとする)
# 入力されたSに対して，この3乗通りの数字が存在し得るかを判定していく
# Sに対してtの1~3桁目を順番に比較していき，3桁ともSに存在すれば，
# カウントする(部分列が存在すると言える)

# 解決方法
# 文字列一致を用いた貪欲法