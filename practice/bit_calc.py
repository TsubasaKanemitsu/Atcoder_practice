x = 10
y = 12

# bit演算
# 1010 + 1100 = 1110
print(x | y)

# 1010 * 1100 = 1000
print(x & y)

# 1010 ^ 1100 = 0110
print(x ^ y)

# 反転 0101 -> -11
print(~x)

# bitシフト
# 左シフト
# x << 2: xを2桁左へシフトする
# 001011(= 11) << 2 -> 101100 = 44
print(11 << 2)
# x >> 2: xを2桁右へシフトする
print(11 >> 2)

#
list = [4, 10, 1]

def bit_plus(list):
    sum = 0
    # 000 ~ 111まで
    for bit in range(1 << len(list)):
        # 0 ~ len(list) == 3
        # bitの各桁に対してビットシフトを用いて各桁とのand(bit * 1)をとることで
        # 計算に含める値を抽出している
        for i in range(len(list)):
            if bit & (1 << i):
                sum += list[i]
    return sum

print(bit_plus(list))