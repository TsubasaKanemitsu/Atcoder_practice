N = int(input())
P = list(map(int, input().split()))
ANS = sorted(P)
count = 0
for i in range(N):
    if P[i] != ANS[i]:
        count += 1

if count <= 2:
    print("YES")
else:
    print("NO")
