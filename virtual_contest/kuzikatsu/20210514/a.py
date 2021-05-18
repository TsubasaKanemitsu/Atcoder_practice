a, b, c = list(map(int, input().split()))

if (a == b and a != c):
    print(c)
elif (b == c and b != a):
    print(a)
elif (a == c and a != b):
    print(b)
