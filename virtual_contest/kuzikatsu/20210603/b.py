n = int(input())
L = list(map(int, input().split()))
ans = 0

for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            if (L[i] != L[j] and L[i] != L[k] and L[j] != L[k]) and max(L[i], L[j], L[k]) < sum([L[i], L[j], L[k]]) - max(L[i], L[j], L[k]):
                ans += 1
print(ans)