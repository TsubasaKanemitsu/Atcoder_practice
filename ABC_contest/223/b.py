S = input()

min_S = []
for i in range(len(S)):
    temp_s = ''
    for j in range(len(S)):
        temp_s += S[(i + j) % len(S)]
    min_S.append(temp_s)

min_S.sort()
print(min_S[0])
print(min_S[-1])
