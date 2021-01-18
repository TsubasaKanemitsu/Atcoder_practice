n = int(input())

p = list(map(int, input().split()))

now = 0
comp = set()
for i in p:
    comp.add(i)
    while now in comp:
        now += 1
    print(now)