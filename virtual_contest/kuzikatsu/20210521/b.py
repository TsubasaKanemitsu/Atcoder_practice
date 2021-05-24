h, w = list(map(int, input().split()))
c = []

for _ in range(h):
    a = list(input())
    c.append(a)
    c.append(a)
for cc in c:
    print(''.join(cc))
