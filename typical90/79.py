h, w = list(map(int, input().split()))
A = [list(map(int, input().split())) for _ in range(h)]
B = [list(map(int, input().split())) for _ in range(h)]

ans = 0
for i in range(h - 1):
    for j in range(w - 1):
        if B[i][j] - A[i][j] == 0:
            continue
        ans += abs(B[i][j] - A[i][j])
        pos = ((0, 1), (1, 0), (1, 1), (0, 0))
        for dx, dy in pos:
            x = j + dx
            y = i + dy
            A[y][x] += (B[i][j] - A[i][j])

for i in range(h):
    for j in range(w):
        if A[i][j] != B[i][j]:
            print("No")
            exit()
print("Yes")
print(ans)