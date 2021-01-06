S = input()
T = input()

ans = len(T)
for i in range(0, len(S) - len(T)):
    diff_count = 0
    for j in range(len(T)):
        if T[i] != S[i + j]:
            diff_count += 1

    ans = min(ans, diff_count)

print(ans)