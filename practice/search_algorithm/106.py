# 5分30秒
n = int(input())

ans = 0
for num in range(1, n + 1, 2):
    count = 0
    for i in range(1, num + 1):
        if num % i == 0:
            count += 1

    if count == 8:
        ans += 1
print(ans)