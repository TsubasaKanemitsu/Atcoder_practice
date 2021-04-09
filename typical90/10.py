n = int(input())

C = [0] * n
P = [0] * n
for i in range(n):
    C[i], P[i] = list(map(int, input().split()))

q = int(input())
L, R = [0] * q, [0] * q
for i in range(q):
    l, r = list(map(int, input().split()))
    L[i] = l - 1
    R[i] = r - 1

one = []
two = []
for i in range(n):
    if C[i] == 1:
        one.append(P[i])
        two.append(0)
    else:
        two.append(P[i])
        one.append(0)

cum_one = [one[0]]
cum_two = [two[0]]
for i in range(1, n):
    cum_one.append(cum_one[i - 1] + one[i])
    cum_two.append(cum_two[i - 1] + two[i])

for i in range(q):
    ans_one = cum_one[R[i]] - cum_one[L[i] - 1]
    ans_two = cum_two[R[i]] - cum_two[L[i] - 1]
    print(ans_one, ans_two)