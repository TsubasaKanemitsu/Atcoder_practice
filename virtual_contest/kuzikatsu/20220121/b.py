n = int(input())
C = list(map(int, input().split()))

# 配列Aは同じ値を持たない
# AiはかならずCi以下になる
# 1 <= Ai <= Ciであるため
# 各Aiがなり得る値はCi個存在するが、
# すでに出現している数字を選択できないので
# 既に出現している値のところは省くように計算する必要がある

# Cの順序は特に問題にならないので
# ソートする

# 前の数値と同じ数字であれば、減算する数が2となる
C.sort()
MOD = 10 ** 9 + 7
ans = 1
# 既に出現している数字の個数
cnt = 0
for i in range(n):
    ans *= (C[i] - cnt)
    ans = ans % MOD
    cnt += 1
print(ans % MOD)