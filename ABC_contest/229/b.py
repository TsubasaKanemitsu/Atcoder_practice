a, b = list(input().split())

for i in range(min(len(a), len(b))):
    ans = int(a[len(a) - i - 1]) + int(b[len(b) - i - 1])
    if ans >= 10:
        print("Hard")
        exit()
print("Easy")