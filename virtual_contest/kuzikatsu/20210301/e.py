# 5で割り切れる正の整数の中で素数なものは5以外にない
# 素数を足し合わせて必ず合成数になる条件を考える

# 割った余りで合成数にできる

import itertools

n = int(input())


prime = []

def is_prime(n):
    if n == 1:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


for i in range(2, 55556):
    if is_prime(i):
        prime.append(i)

result = []
for i in range(len(prime)):
    if prime[i] % 5 == 1:
        result.append(str(prime[i]))

print(' '.join(result[0:n]))

