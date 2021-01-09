s = int(input())

A = [s]

def solve(n):
    if n % 2 == 0:
        n = n // 2
    else:
        n = 3 * n + 1

    return n

i = 1
while True:
    a = solve(A[i - 1])
    if a in set(A):
        i += 1
        print(i)
        break
    A.append(a)
    i += 1