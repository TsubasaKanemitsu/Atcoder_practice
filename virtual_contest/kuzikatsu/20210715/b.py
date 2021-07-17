t = int(input())

ans = []
for i in range(t):
    l, r = list(map(int, input().split()))
    c = r - l
    x = (c - l) + 1
    if x < 0:
        x = 0
    ans.append(x * (x + 1) // 2)

for a in ans:
    print(a)
    