# ABC 183C
import itertools
n, k = list(map(int, input().split()))
T = [list(map(int, input().split())) for _ in range(n)]

l = [i for i in range(1, n)]

cnt = 0
for perm in itertools.permutations(l):
    perm = [0] + list(perm)
    ans = 0
    # 最初は町1からx, 途中はx・・・y, で最後は町y -> 1に
    # 移動するようにする
    for i in range(n):
        ans += T[perm[i]][perm[(i + 1) % n]]
    
    if ans == k:
        # print(perm)
        cnt += 1
print(cnt)