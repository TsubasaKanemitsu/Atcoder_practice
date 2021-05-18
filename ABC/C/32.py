n, k = list(map(int, input().split()))
s = [int(input()) for _ in range(n)]

if s.count(0) >= 1:
    print(n)
    exit()

right = 0
ans = 0
mul = 1
for i in range(n):
    left = i
    while right < n and mul * s[right] <= k:
        mul *= s[right]
        right += 1

    ans = max(ans, right - left)

    if left == right:
        right += 1
    else:
        mul /= s[left]
print(ans)