n = int(input())

six = [0]
nine = [0]

dp = [10 ** 18] * (n + 1)
dp[0] = 0
flag = [False] * (n + 1)
flag[0] = True

for i in range(1, 10):
    six.append(6 ** i)
    nine.append(9 ** i)

for i in range(n):
    if not flag[i]:
        continue

    if i + 1 <= n:
        # print("1")
        flag[i + 1] = True
        dp[i + 1] = min(dp[i + 1], dp[i] + 1)

    for j in range(len(nine)):
        if i + nine[j] <= n:
            flag[i + nine[j]] = True
            # print(dp[i] + j)
            dp[i + nine[j]] = min(dp[i + nine[j]], dp[i] + 1)
    
    for j in range(len(six)):
        if i + six[j] <= n:
            # print("6")
            flag[i + six[j]] = True
            dp[i + six[j]] = min(dp[i + six[j]], dp[i] + 1)
print(dp[-1])