# Nが少ない場合の数え上げの具体例を考えてみる
# 考察方法の訓練 (https://atcoder.jp/contests/arc117/editorial/1111)

n = int(input())
A = list(map(int, input().split()))
A.sort()
ans = A[0] + 1
for i in range(1, n):
    ans *= (A[i] - A[i - 1] + 1) % (10 ** 9 + 7)
print(ans % (10 ** 9 + 7))