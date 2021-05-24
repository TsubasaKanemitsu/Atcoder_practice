n, q = list(map(int, input().split()))
A = list(map(int, input().split()))

shift = 0
ans = []
for i in range(q):
    t, x, y = list(map(int, input().split()))
    x -= 1
    y -= 1
    if t == 1:
        x -= shift
        y -= shift
        if x < 0:
            x = n + x
        if y < 0:
            y = n + y
        temp = A[x]
        A[x] = A[y]
        A[y] = temp
        
    elif t == 2:
        shift += 1
        if shift == n:
            shift = 0
    else:
        x -= shift
        y -= shift
        if x < 0:
            x = n + x
        if y < 0:
            y = n + y
        ans.append(A[x])

for a in ans:
    print(a)