# 31分
n = int(input())
a = list(map(int, input().split()))
a.sort(reverse=True)
ans = a[0]

for i in range(1, n // 2):
    ans += a[i] * 2
if (n % 2 == 1):
    ans += a[i + 1]
print(ans)