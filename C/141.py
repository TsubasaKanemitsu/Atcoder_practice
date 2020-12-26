n, k, Q = list(map(int, input().split()))

point = [0 for i in range(n)]
record = {}
for i in range(Q):
    ans_q = int(input())
    point[ans_q - 1] += 1

point = [i + k - Q for i in point]

for p in point:
    if p > 0:
        print("Yes")
    else:
        print("No")