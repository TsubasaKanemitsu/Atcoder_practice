n = int(input())
B = [list(map(int, input().split())) for _ in range(n)]

for b in B:
    a1 = b[0]
    a2 = b[1]
    a3 = b[-1] - a1 - a2
    print(a1, a2, a3)
