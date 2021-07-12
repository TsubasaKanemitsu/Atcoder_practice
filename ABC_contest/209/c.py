n = int(input())
C = list(map(int, input().split()))

C.sort()

diff = []

min_c = min(C)
ans = 1
for i in range(n):
    if i == 0:
        ans *= min_c
    else:
        ans = (ans * (((C[i] - min_c) + (min_c - i)))) % (10 ** 9 + 7)

ans = ans % (10 ** 9 + 7)

print(ans)