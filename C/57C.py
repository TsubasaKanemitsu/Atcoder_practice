N = int(input())
F_AB = len(str(N))
A = 1
while A * A <= N:
    if N % A == 0:
        B = int(N / A)
        temp_F_AB = max(len(str(A)), len(str(B)))
        if F_AB > temp_F_AB:
            F_AB = temp_F_AB
    A += 1

print(F_AB)

# 計算のオーダを意識する
# どういう条件でループを回せば，制限時間内で収まるかを考える
