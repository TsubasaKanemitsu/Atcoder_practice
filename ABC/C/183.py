import itertools
n, k = list(map(int, input().split()))

T = []

for i in range(n):
    T.extend([list(map(int, input().split()))])

perm = []
perm_list = [i for i in range(0, n)]

# 都市の経路の組み合わせ
for p in itertools.permutations(perm_list, len(perm_list)):
    if p[0] == 0:
        p = list(p)
        p.append(0)
        perm.append(p)
# 位置情報取得
def get_pos(l):
    pos = []
    for i in range(len(l) - 1):
        pos.extend([[l[i], l[i + 1]]])
    return pos

count = 0
for pe in perm:
    sum_val = 0
    pos = get_pos(pe)
    for ps in pos:
        sum_val += T[ps[0]][ps[1]]
    if sum_val == k:
        count += 1
print(count)