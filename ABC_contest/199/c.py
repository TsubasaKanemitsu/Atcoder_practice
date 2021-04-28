n = int(input())
s = list(input())
q = int(input())
TAB = [list(map(int, input().split())) for _ in range(q)]

cnt = 0
add = 0
for i in range(q):
    t, a, b = TAB[i]
    a -= 1
    b -= 1

    if cnt % 2 == 1:
        add = n
    else:
        add = 0

    if t == 1:
        b = b + add
        a = a + add
        if a >= 2 * n:
            a = a - (2 * n)
        if b >= 2 * n:
            b = b - (2 * n)
        
        temp = s[b]
        s[b] = s[a]
        s[a] = temp
    elif t == 2:
        cnt += 1

f_s = s[:n]
b_s = s[n:]
if cnt % 2 == 1:
    s = ''.join(b_s) + ''.join(f_s)
    print(s) 
else:
    print(''.join(s))

