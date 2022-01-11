import itertools
n = int(input())
P = tuple(map(int, input().split()))
Q = tuple(map(int, input().split()))

num = [i for i in range(1, n + 1)]

a = 0
cnt = 0
for perm in itertools.permutations(num):
    p_flag = True
    q_flag = True
    for i in range(n):
        if not perm[i] == P[i]:
            p_flag = False
            break
    if p_flag:
        a = cnt

    for i in range(n):
        if not perm[i] == Q[i]:
            q_flag = False
            break
    if q_flag:
        b = cnt
    
    cnt += 1

print(abs(a - b))