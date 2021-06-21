N, k = list(map(int, input().split()))
D = list(input().split())

num = set(D)

for i in range(10 ** 5 + 1):
    ans = N + i
    if len(set(str(ans)) & num) == 0:
        print(ans)
        exit()