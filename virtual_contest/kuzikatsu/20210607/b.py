a, b, c = list(map(int, input().split()))
v = [a, b, c]

odd = 0
even = 0

for n in v:
    if n % 2 == 0:
        even += 1
    else:
        odd += 1

ans = 0
if odd == 2:
    for i in range(3):
        if v[i] % 2 == 1:
            v[i] += 1
    ans += 1
elif even == 2:
    for i in range(3):
        if v[i] % 2 == 0:
            v[i] += 1
    ans += 1
v.sort()

ans += (v[2] - v[1]) // 2 + (v[2] - v[0]) // 2
print(ans)