# ABC 51 B
# 5 min
# 工夫した全探索

k, s = list(map(int, input().split()))

ans = 0
for x in range(k + 1):
    for y in range(k + 1):
        z = s - x - y
        if 0 <= z <= k:
            ans += 1
print(ans)