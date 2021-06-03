# 15分
# DPかな?
# 漸化式を立てて，DP


n, L = list(map(int, input().split()))

stair = [0] * (n + 1)
stair[0] = 1
for i in range(n + 1):
    if i + 1 <= n:
        stair[i + 1] += stair[i]
    if i + L <= n:
        stair[i + L] += stair[i]

ans = stair[-1] % (10 ** 9 + 7)
print(ans)