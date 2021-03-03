a, b, c = list(map(int, input().split()))

if a % 2 == 1 and b % 2 == 1 and c % 2 == 1:
    num = [a, b, c]
    num.sort()
    print(num[0] * num[1])
else:
    print(0)