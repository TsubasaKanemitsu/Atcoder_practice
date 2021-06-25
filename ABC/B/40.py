# 13分
# 工夫した全探索

n = int(input())

ans = 10 ** 99
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i * j > n:
            break
        ans = min(ans, n - i * j + abs(i - j))
print(ans)