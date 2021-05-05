import itertools
N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
M = int(input())
XY = [tuple(input().split()) for _ in range(M)]

xy = set()
for x, y in XY:
    xy.add(f'{x}:{y}')
    xy.add(f'{y}:{x}')
    
ans = 10 ** 99
for perm in itertools.permutations([i for i in range(1, N + 1)]):
    flag = True
    for i in range(len(perm) - 1):
        p1 = str(perm[i]) + ':' + str(perm[i + 1])
        p2 = str(perm[i + 1]) + ':' + str(perm[i])
        if p1 in xy or p2 in xy:
            flag = False
            break
    if flag:
        temp_ans = 0
        for i in range(len(perm)):
            temp_ans += A[perm[i] - 1][i]
        ans = min(temp_ans, ans)
        
if ans == 10 ** 99:
    print(-1)
    exit()
print(ans)