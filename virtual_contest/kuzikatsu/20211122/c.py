n, l, r = list(map(int, input().split()))

# xとNのXORがN未満になるxの個数は?
# L <= x <= R
# 制約
# 1. 1 <= N <= 10 ** 18
# 2. 1 <= L <= R <= 10 ** 18

# 考察
# 1. 制約1, 2よりO(N)探索は無理
# XORの法則を見出す必要がありそう

# Nより小さくなるXORを生み出すXの値はNの最大ビット位置と同じ場所に1がくる数字が
# 最大のXとなる
# R - Xが答えとなる


bit = []

while n > 0:
    bit.append(n % 2)
    n = n // 2

bit_pos = 0
for i in range(len(bit)):
    if bit[i] == 1:
        bit_pos = i

max_x = 2 ** i
print(max_x)
if max_x < l:
    print("i")
    print(0)
elif l <= max_x <= r:
    print("j")
    print(r - max_x - 1)
else:
    print("k")
    print(r - l)
# ok = set()
# no = set()
# for i in range(l, r + 1):
#     xor = i ^ n
#     if xor < n:
#         ok.add(i)
#     else:
#         no.add(i)
#     print(f"i:{i}", xor)

# print(ok)
# print(no)
