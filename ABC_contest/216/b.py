n = int(input())

S = []
for i in range(n):
    s, t = input().split()
    S.append(s + '-' + t)

for i in range(n):
    for j in range(i + 1, n):
        if S[i] == S[j]:
            print("Yes")
            exit()
print("No")