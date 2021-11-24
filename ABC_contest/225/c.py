n, m = list(map(int, input().split()))

B = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(m - 1):
        front = B[i][j] % 7
        if front == 0:
            front = 7
        front += 1

        back = B[i][j + 1] % 7
        if back == 0:
            back = 7

        if front != back or B[i][j] + 1 != B[i][j + 1]:
            print("No")
            exit()

for j in range(m):
    for i in range(n - 1):
        if B[i][j] + 7 != B[i + 1][j]:
            print("No")
            exit()
print("Yes")
