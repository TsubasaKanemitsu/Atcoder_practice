from collections import defaultdict
n = int(input())
A = list(map(int, input().split()))

max_a = max(A)
cnt = defaultdict(int)

for a in A:
    cnt[a] += 1

flag = [True] * (max_a + 1)

A = sorted(set(A))

for a in A:
    if cnt[a] > 1:
        flag[a] = False
    # Aの最大値までのaの約数が存在すれば, Falseにする
    for i in range(2 * a, max_a + 1, a):
        flag[i] = False

res = 0
for a in A:
    if flag[a]:
        res += 1
print(res)