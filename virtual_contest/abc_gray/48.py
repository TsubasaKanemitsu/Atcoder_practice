# ABC 195 C
# 5分

n = int(input())

ans = 0

if n < 1000:
    print(0)
    exit()

for i in range(3, 16, 3):
    if 10 ** i <= n <= 10 ** (i + 3) - 1:
        ans += (n - (10 ** i - 1)) * (i // 3)
        print(ans)
        exit()
    else:
        ans += (10 ** (i + 3) - 10 ** i) * (i // 3)
print(ans)