n = int(input())
p = [int(input()) for _ in range(n)]

max_v = max(p) // 2
ans = sum(p) - max(p) + max_v
print(ans)