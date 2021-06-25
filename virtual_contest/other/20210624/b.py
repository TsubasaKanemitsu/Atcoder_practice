a, b, c = list(map(int, input().split()))
a, b, c = sorted([a, b, c])

if a == b == c:
    print("Yes")
else:
    print("No")