n = int(input())

A = list(map(int, input().split()))

cnt = 0
for a in A:
    if a < 0:
        cnt += 1

if cnt % 2 == 0:
    ans = 0
    for a in A:
        ans += abs(a)
    print(ans)
else:
    ans = 0
    min_val = 10 ** 10 + 1
    for a in A:
        ans += abs(a)
        min_val = min(min_val, abs(a))
    ans -= 2 * min_val
    print(ans)