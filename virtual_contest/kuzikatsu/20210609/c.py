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


dp = [10 ** 9] * (n + 1)
dp[1] = 1

for i in range(2, n + 1):
    # 約数全列挙
    j = divisor(i)[-2]
    # jがiの約数の場合 = 現在のiより1つ前の約数 + 1しないといけない
    # 約数全列挙の一番最後は，自分自身なのでその1つ前が，jとなる
    # jの時の数値と被ってはいけないので，dp[j] + 1している
    dp[i] = dp[j] + 1 

for i in range(1, n + 1):
    print(dp[i], end=" ")