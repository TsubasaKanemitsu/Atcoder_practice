n = int(input())

ans = 0

for i in range(3, 16, 3):
    if n - int(str(9) * i) > 0:
        ans += n - int(str(9) * i)
print(ans)