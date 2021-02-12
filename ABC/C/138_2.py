# 6分
n = int(input())
v = list(map(float, input().split()))

v.sort()

ans = v[0]
for i in range(1, n):
    ans = (ans + v[i]) / 2
print(ans)