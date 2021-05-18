a, b = list(map(int, input().split()))

half = (a + b) / 2

if half.is_integer():
    print(int(half))
else:
    print("IMPOSSIBLE")