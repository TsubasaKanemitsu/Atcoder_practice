from collections import defaultdict
n = int(input())
A = list(map(int, input().split()))
Q = int(input())

BC = [list(map(int, input().split())) for _ in range(Q)]

cnt_a = defaultdict(int)

for a in A:
    cnt_a[a] += 1

add = 0
for k, v in cnt_a.items():
    add += k * v


ans = []
for bc in BC:
    temp = cnt_a[bc[0]]
    # 置き換え前
    val1 = temp * bc[0]
    val2 = bc[1] * temp
    # 置き換え後
    cnt_a[bc[1]] += temp
    cnt_a[bc[0]] = 0
    add = add + (val2 - val1)
    print(add)
