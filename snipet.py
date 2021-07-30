# 10進数をn進数に変換
def Base_10_to_n(n, b):
    if n // b:
        return Base_10_to_n(n // b, b) + str(n % b)
    return str(n % b)

# 重複なし3重ループ


def triple_roop(n):
    for i in range(1, n - 1):
        for j in range(i + 1, n):
            for k in range(j + 1, n + 1):
                print(i, j, k)

# 素数判定


def is_prime(n):
    if n == 1:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

# 約数列挙


def divisor(n):
    i = 1
    divisor_list = []
    while i * i <= n:
        if n % i == 0:
            divisor_list.append(i)
            if n // i != i:
                divisor_list.append(n // i)
        i += 1
    divisor_list.sort()
    return divisor_list

# 最大公約数
# mathライブラリのmath.gcd(x, y)も使える


def gcd(a, b):
    if a < b:
        a, b = b, a
    while a % b > 0:
        a, b = b, a % b

    return b

# フェルマーの小定理(a, modは互いに素でなければならない)
# 高速に逆元を求める


def fermat(a, mod):
    return pow(a, mod - 2, mod)


# 拡張ユークリッド互除法
# aの逆元を高速で求める
def extgcd(a, b):
    if b:
        d, y, x = extgcd(b, a % b)
        y -= (a // b) * x
        return d, x, y
    return a, 1, 0


# 最小公倍数
def lcm(x, y):
    import math
    return (x * y) // math.gcd(x, y)

# 組み合わせ総数


def combinations_count(n, r):
    import math
    return math.factorial(n) // ((math.factorial(n - r)) * math.factorial(r))

# 順列総数


def permutaions_count(n, r):
    import math
    return math.factorial(n) // math.factorial(n - r)


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


class UnionFind():
    def __init__(self, n):
        self.parents = [-1] * n
        # self.n = n

    # 親を見つける
    def find(self, x):
        # 頂点の場合
        if self.parents[x] < 0:
            return x
        # 子頂点の場合，親の頂点をparentsに格納する
        else:
            # 経路圧縮
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        # x, yの頂点を探す
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return 0

        # xの頂点がyの頂点より大きい場合, 入れ替える
        if self.parents[x] > self.parents[y]:
            x, y = y, x

        # 頂点x, yを結合する
        self.parents[x] += self.parents[y]
        self.parents[y] = x

    # def same(self, x, y):
    #     return self.find(x) == self.find(y)

    def size(self, x):
        return - 1 * self.parents[x]

    # def groups():
    #     out_dict = defaultdict(list)
    #     for i in range(self.n):
    #         parent = self.find(i)
    #         out_dict[parent].append(i)
    # return out_dict
    # rn out_dict


def factorization(n):
    i = 2
    result = []
    while i * i <= n:
        if n % i == 0:
            ex = 0
            while n % i == 0:
                ex += 1
                n = n // i
            result.append((i, ex))
        i += 1

    if n != 1:
        result.append((n, 1))

    return result

