# 10分
# 1WA
# 全探索の値更新

n, k = list(map(int, input().split()))

H = [int(input()) for _ in range(n)]

H.sort(reverse=True)

ans = 10 ** 20

for i in range(n - k + 1):
    ans = min(ans, abs(H[i] - H[i + k - 1]))
print(ans)