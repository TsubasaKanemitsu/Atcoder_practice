n, m = list(map(int, input().split()))
A = list(map(int, input().split()))

def prime_numbers(m):
    # 素数を保持するset
    primes = set()

    # 2以上m以下の素数を数え上げる
    n = 2
    while n <= m:
        # 自身より小さい全ての素数で割り切れなければ、素数とみなせる
        if all(n % i != 0 for i in primes):
            primes.add(n)
        n += 1

    return primes


primes = set([1] + list(prime_numbers(m)))

print(primes)
ans = []
set_a = set(A)
for p in list(primes):
    flag = True
    for i in range(n):
        if p in set_a:
            flag = False
    if flag:
        ans.append(p)
        
print(ans)
new_ans = []
for a in ans:
    cnt = 0
    if a == 1:
        new_ans.append(a)
        continue
    while a ** cnt <= m:
        new_ans.append(a ** cnt)
        cnt += 1

print(len(new_ans))
# for a in new_ans:
#     print(a)
