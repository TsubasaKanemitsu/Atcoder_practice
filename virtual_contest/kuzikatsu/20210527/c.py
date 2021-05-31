n = int(input())

pushed = [False] * n

A = [int(input()) for _ in range(n)]

now = A[0] - 1
pushed[0] = True
cnt = 1
while True:
    if not pushed[now]:
        if now == 1:
            print(cnt)
            exit()
        pushed[now] = True
        now = A[now] - 1
        cnt += 1
    else:
        print(-1)
        exit()