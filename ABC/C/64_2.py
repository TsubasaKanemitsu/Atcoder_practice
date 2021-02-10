n = int(input())

A = list(map(int, input().split()))

color = []
fr_cnt = 0
for a in A:
    if a >= 3200:
        fr_cnt += 1
    else:
        color.append(a // 400)
upper = len(set(color)) + fr_cnt
print(max(1, len(set(color))), upper)