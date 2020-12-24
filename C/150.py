import itertools
n = int(input())
p = tuple(map(int, input().split()))
q = tuple(map(int, input().split()))

seq = [i for i in range(1, n + 1)]
perm = list(itertools.permutations(seq))

p_index = perm.index(p) + 1
q_index = perm.index(q) + 1

ans = abs(p_index - q_index)
print(ans)
