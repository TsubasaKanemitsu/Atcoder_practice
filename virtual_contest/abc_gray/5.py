# 詰まった
# 5分?
n = int(input())
d = list(map(int, input().split()))

d.sort()

ans = d[n // 2] - d[n // 2 - 1]
print(ans)