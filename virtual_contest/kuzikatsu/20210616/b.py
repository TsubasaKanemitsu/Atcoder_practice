a, b , k = list(map(int, input().split()))

cnt = 0
for i in range(100, -1, -1):
    if a % i == 0 and b % i == 0 and i <= a and i <= b:
        cnt += 1
        if cnt == k:
            print(i)
            exit()
