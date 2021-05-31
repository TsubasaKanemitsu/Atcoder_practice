n = int(input())
s = list(input())
q = int(input())

cnt = 0
for i in range(q):
    t, a, b = list(map(int, input().split()))
    a -= 1
    b -= 1
    if t == 1:
        if cnt % 2 == 1:
            a += n
            b += n
        if a >= 2 * n:
            a = a - 2 * n
        if b >= 2 * n:
            b = b - 2 * n
        temp = s[a]
        s[a] = s[b]
        s[b] = temp
    else:
        cnt += 1

ans = []
if cnt % 2 == 1:
    ans = ''.join(s[n:]) + ''.join(s[0:n])
else:
    ans = ''.join(s)
print(ans)