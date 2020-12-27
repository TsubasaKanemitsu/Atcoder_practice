n, d = list(map(int, input().split()))

for i in range(1, n + 1):
    if (1 + d * 2) * (i) >= n:
        print(i)
        break
