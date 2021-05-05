# 12分
# 累積和はTLE
# 大きい数値の掛け算と割り算はTLEになる可能性がある．
# 数列の法則性でどのパターンが条件を満たすかを言い換える必要がある．
n, k = list(map(int, input().split()))
A = list(map(int, input().split()))

for i in range(k, n):
    if A[i - k] < A[i]:
        print("Yes")
    else:
        print("No")
    