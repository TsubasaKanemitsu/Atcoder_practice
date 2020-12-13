N = int(input())

A = [i for i in range(1, N + 1)]
matched = []
for a in A:
    if a % 3 == 0 and a % 5 == 0:
        pass
    elif a % 3 == 0:
        pass
    elif a % 5 == 0:
        pass
    else:
        matched.append(a)

ans = sum(matched)

print(ans)