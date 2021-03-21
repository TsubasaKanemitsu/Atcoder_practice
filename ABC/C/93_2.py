a, b, c = list(map(int, input().split()))

max_val = max(a, b, c)

if max_val * 3 % 2 == (a + b + c) % 2:
    print((((max_val * 3) - (a + b + c)) // 2))
else:
    print(((max_val + 1) * 3 - (a + b + c)) // 2)
