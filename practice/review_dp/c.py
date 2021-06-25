# やり直し

n = int(input())
ABC = [list(map(int, input().split())) for _ in range(n)]
ABC.insert(0, [0, 0, 0])

happy = [[0] * 3 for _ in range(n + 1)]

for i in range(1, n + 1):
    ta, tb, tc = happy[i]
    ha, hb, hc = happy[i - 1]
    a, b, c = ABC[i]
    happy[i][0] = max(ta, hb + b, hc + c)
    happy[i][1] = max(tb, ha + a, hc + c)
    happy[i][2] = max(tc, ha + a, hb + b)

print(max(happy[n]))