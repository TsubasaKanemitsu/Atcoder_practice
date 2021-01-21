a, b, c = list(map(int, input().split()))

i = 1
num = 0
while i <= b:
    num += a
    # print(num)
    if num % b == c:
        print("YES")
        exit()
    i += 1
print("NO")