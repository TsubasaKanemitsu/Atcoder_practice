n = int(input())
a = list(map(int, input().split()))

ans = 0
right = 1
for i in range(n):
    left = i
    while right < n and (right <= left or a[right - 1] < a[right]):
        right += 1
    ans += right - left

    if left == right:
        right += 1

print(ans)