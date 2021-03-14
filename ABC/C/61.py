n, k = list(map(int, input().split()))

ab = []
for i in range(n):
    a, b = list(map(int, input().split()))
    ab.append([a, b])

ab.sort(key=lambda x:x[0])

prev = 1
now = 0
for i in range(len(ab)):
    now += ab[i][1]
    if prev <= k <= now:
        print(ab[i][0])
        exit()
    prev = now

