N = int(input())
L_stick = list(map(int, input().split()))
L_stick.sort()
ans = 0
for i in range(N):
    for j in range(i):
        for k in range(j):
            if L_stick[k] != L_stick[j] and L_stick[i] != L_stick[j] \
                and L_stick[k] + L_stick[j] > L_stick[i]:
                ans += 1

print(ans)