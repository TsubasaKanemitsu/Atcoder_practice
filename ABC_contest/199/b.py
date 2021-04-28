n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
cnt = 0
left = a[0]
right = b[0]
for i in range(n):
    left = max(a[i], left)
    right = min(right, b[i])

ans = right - left + 1
if ans < 0:
    ans = 0
print(ans)