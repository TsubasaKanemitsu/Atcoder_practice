# 問題文の読み間違い

a, b, c = list(map(int, input().split()))

if a % 2 == 1 or b % 2 == 1 or c % 2 == 1:
    print(0)
    exit()

if a == b == c:
    print(-1)
    exit()

cnt = 0
# 最大値と最小値の差が1 / 2ずつ縮まっていくので，差が0になるのはO(logM) で
# 求めることができる
# 今回の問題で差が0になるので全ての値が同じ(= 全て奇数になる)ということなので
# それまでに必ず奇数が出現する
# よって，ループ処理が終わることは確実である．
while a % 2 == 0 and b % 2 == 0 and c % 2 == 0:
    
    half_a = a // 2
    half_b = b // 2
    half_c = c // 2
    
    a = half_a + half_b
    b = half_b + half_c
    c = half_c + half_a
    cnt += 1
print(cnt)