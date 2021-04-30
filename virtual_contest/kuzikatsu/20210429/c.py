n = int(input())
AB = [list(map(int, input().split())) for _ in range(n)]

AB.sort(key=lambda x: x[1])

time = 0
for i in range(n):
    a, b = AB[i]
    time += a
    if time > b:
        print("No")
        exit()
print("Yes")