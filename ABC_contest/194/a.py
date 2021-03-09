a, b = list(map(int, input().split()))

aa = a + b

if aa >= 15 and b >= 8:
    print(1)
elif aa >= 10 and b >= 3:
    print(2)
elif aa >= 3:
    print(3)
else:
    print(4)