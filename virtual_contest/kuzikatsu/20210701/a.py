a, b = list(map(int, input().split()))

if abs(a - b) % 2 == 0:
    print(abs(a - b) // 2 + min(a, b))
else:
    print("IMPOSSIBLE")