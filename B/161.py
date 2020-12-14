N, M = list(map(int, input().split()))

A = list(map(int, input().split()))

matched = [a for a in A if a >= sum(A) * 1 / (4 * M)]
if len(matched) >= M:
    print("Yes")
else:
    print("No")