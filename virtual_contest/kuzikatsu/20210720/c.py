n = int(input())
s = list(input())
q = int(input())
flag = 0
for _ in range(q):
    t, a, b = list(map(int, input().split()))
    if t == 1:
        a -= 1
        b -= 1
        if flag % 2 == 1:
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
        flag += 1

if flag % 2 == 1:
    ans = ''.join(s[n:]) + ''.join(s[0:n])
    print(ans)
else:
    print(''.join(s))