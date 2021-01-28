s, p = list(map(int, input().split()))


def p_solve(p):
    i = 1
    n = []
    m = []
    while i * i <= p:
        if p % i == 0:
            n.append(i)
            m.append(p//i)
        i += 1
    return n, m

n, m = p_solve(p)

if len(n) == 0:
    print("No")
else:
    for i in range(len(n)):
        if n[i] + m[i] == s:
            print("Yes")
            exit()
    print("No")