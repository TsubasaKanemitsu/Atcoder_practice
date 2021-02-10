n = int(input())
x = list(map(int, input().split()))

_x = sorted(x)

for i in range(n):
    if x[i] <= _x[n // 2 - 1]:
        print(_x[n // 2])
    elif x[i] >= _x[n // 2]:
        print(_x[n // 2 - 1])
