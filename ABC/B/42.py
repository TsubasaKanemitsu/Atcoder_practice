n, l = list(map(int, input().split()))

s = [input() for _ in range(n)]

s = sorted(s)
print(''.join(s))