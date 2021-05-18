n = int(input())

i = 1
ans1 = 0
ans2 = 0
ans = 10 ** 99
while i * i <= n:
    if n % i == 0:
        ans1 = n // i
        ans2 = i
        ans = min(ans1 + ans2 - 2, ans)
    i += 1
print(ans)