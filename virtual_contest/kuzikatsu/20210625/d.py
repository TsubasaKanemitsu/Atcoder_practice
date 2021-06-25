from collections import defaultdict

N, M = list(map(int, input().split()))
PY = [list(map(int, input().split())) for _ in range(M)]

prefectures = defaultdict(list)

for i in range(M):
    p, y = PY[i]
    prefectures[p].append((i + 1, y))

ans = []
for i in range(N):
    P = sorted(prefectures[i + 1], key=lambda x:x[1])
    for j in range(len(P)):
        city, year = P[j]
        prefecture = i + 1
        ans.append((city, str(prefecture).zfill(6) + str(j + 1).zfill(6)))

ans.sort()

for city, ID in ans:
    print(ID)