# 33分
# 累積和 & 高速素数演算
# 区間の個数を求めるときは，累積和でO(1)で求める
# 素数となる値を求めたいので，素数演算は高速に行う

q = int(input())
LR = [list(map(int, input().split())) for _ in range(q)]

prime = [0] * (10 ** 5 + 1)

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


for i in range(1, 10 ** 5 + 1):
    if i % 2 == 1 and is_prime(i) and is_prime((i + 1) / 2):
        prime[i] = 1

# 連続した素数の累積和
prime_cum_sum = [0]
for i in range(1, 10 ** 5 + 1):
    prime_cum_sum.append(prime_cum_sum[i - 1] + prime[i])

# 累積和で該当する素数の個数をO(1)で求める
for i in range(q):
    l, r = LR[i]
    l -= 1
    print(prime_cum_sum[r] - prime_cum_sum[l])
