n = int(input())

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

ans = divisor(n)
for num in ans:
    print(num)

# 約数を列挙する問題
# 1 <= N <= 10 ^ 12なので全探索はTLEになる
# 約数の列挙はO(N)ではなく，O(√N)で可能となる
# 端的に言うと，小さい数で割り切れる場合，その時の商は大きい数となる
# その大きい数は割り切れる値であるので，小さい数で割り切れたときの商も
# 約数として含めることができる．