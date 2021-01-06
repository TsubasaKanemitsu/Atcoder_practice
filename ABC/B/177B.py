S = list(input())
T = list(input())

count = len(T)
for i in range(len(S) - len(T) + 1):
    temp_count = 0
    for j in range(len(T)):
        if S[i + j] != T[j]:
            temp_count += 1
    count = min(temp_count, count)

print(count)