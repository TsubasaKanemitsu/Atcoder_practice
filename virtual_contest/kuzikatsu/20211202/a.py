n = int(input())
S = list(map(int, input().split()))

flag = [False] * (10 ** 3 + 1) 

for a in range(1, 301):
    for b in range(1, 301):
        c = 3 * a + 3 * b + 4 * a * b
        if c > 1000:
            break
        flag[c] = True

ans = 0
for s in S:
    if not flag[s]:
        ans += 1
print(ans)