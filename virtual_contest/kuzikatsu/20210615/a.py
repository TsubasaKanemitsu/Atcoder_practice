n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

left = a[0]
right = b[0]
for i in range(1, n):
    left = max(left, a[i])
    right = min(right, b[i])

if right < left:
    print(0)
else:
    print(right - left + 1)