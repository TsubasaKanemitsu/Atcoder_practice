a, b, c = list(map(int, input().split()))

if a == b == c:
    print(a)
elif a == b and a != c:
    print(c)
elif a == c and a != b:
    print(b)
elif b == c and b != a:
    print(a)
else:
    print(0)