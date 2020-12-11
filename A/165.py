k = int(input())
a, b = list(map(int, input().split()))

result = "NG"
for i in range(a, b + 1):
    if i % k == 0:
        result = "OK"
        break

print(result)