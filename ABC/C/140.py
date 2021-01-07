n = int(input())


B = (list(map(int, input().split())))

sum_val = 0

C = [B[0]]
for i in range(1, n - 1):
    C.append(min(B[i - 1], B[i]))
C.append(B[-1])

print(sum(C))

