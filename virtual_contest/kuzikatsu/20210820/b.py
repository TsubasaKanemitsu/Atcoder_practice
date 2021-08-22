n = int(input())

sheat = [0] * 10 ** 5
for i in range(n):
    L, R = list(map(int, input().split()))
    L -= 1
    R -= 1
    if (L == R == 10 ** 5 - 1) or R == 10 ** 5 - 1:
        sheat[L] += 1
    else:
        sheat[L] += 1
        sheat[R + 1] -= 1

for i in range(10 ** 5 - 1):
    sheat[i + 1] += sheat[i]

print(sum(sheat))