a, b, x = list(map(int, input().split()))


for i in range(a, a + b + 1):
    if i == x:
        print("YES")
        exit()
print("NO")