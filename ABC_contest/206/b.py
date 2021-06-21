n = int(input())

ans = 0

for i in range(1, 10 ** 5 + 1):
    ans += i
    if ans >= n:
        print(i)
        exit()
