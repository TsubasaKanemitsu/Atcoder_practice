# 8分
import itertools
n = int(input())
p = tuple(map(int, input().split()))
q = tuple(map(int, input().split()))

p_num = 0
q_num = 0
cnt = 1
for perm in itertools.permutations([i + 1 for i in range(n)]):
    if perm == p:
        p_num = cnt
    if perm == q:
        q_num = cnt
    cnt += 1
print(abs(p_num - q_num))
