# https://mathtrain.jp/factorization2
# 20分
# 正当な解法ではない
# A, Bのとりうる最大値がわからなかったので無理やり因数分解の式から求めた
x = int(input())

for a in range(- 300, 300):
    for b in range(-300, 300):
        if a != 0 or b != 0:
            ans = (a - b) * (a ** 4 + a ** 3 * b + a ** 2 * b ** 2 + a * b ** 3 + b ** 4)
            if ans == x:
                print(a, b)
                exit()