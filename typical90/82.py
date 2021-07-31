# 典型90
# 24分

# 考察
# STEP1
# L, Rは1 <= L, R <= 10 ** 18なので
# 愚直に計算するのはTLEになる
# STEP2
# 同じ桁数の数値は同時に文字数を加算していきたい
# L ~ 10 ** ? - 1までが同じ桁の数値の数になるので
# 桁数 * L ~ 10 ** ? - 1までの総和で計算すれば
# 同じ桁で発生する文字数を加算できそうである
# STEP3
# L ~ 10 ** ? - 1までの総和を求めるには、総和の公式を利用すればいい

L, R = list(map(int, input().split()))
mod = (10 ** 9 + 7)
ans = 0

now_length = len(str(L))
now_l = L
cnt = 0
while True:
    left = now_l
    right = 10 ** now_length - 1
    if R >= right:
        cnt += (right * (right + 1) // 2 - left * (left - 1) // 2) * now_length % mod
    else:
        cnt += (R * (R + 1) // 2 - left * (left - 1) // 2) * now_length % mod
        print(cnt % mod)
        exit()
    now_l = right + 1
    now_length = len(str(left))