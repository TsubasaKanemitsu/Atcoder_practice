x = int(input())

b = 1
p = 2

ans = 0
for b in range(1, x + 1):
    for p in range(2, 11):
        if b == 1:
            ans = max(ans, 1)
            break
        if b ** p <= x:
            ans = max(ans, b ** p)
print(ans)