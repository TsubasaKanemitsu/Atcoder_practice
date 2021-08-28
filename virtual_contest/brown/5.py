# ABC 171 E (Red Scarf)
# 12分

# XORの性質

# 偶数個同じ数字を持つとき0になる
# 同じ数字でxorをとると0になる

# 奇数個だと1になる

n = int(input())
A = list(map(int, input().split()))
B = []

b_xor = A[0]
for i in range(1, n):
    b_xor ^= A[i]

for i in range(n):
    B.append(b_xor ^ A[i])

for i in range(n):
    print(B[i], end=' ')