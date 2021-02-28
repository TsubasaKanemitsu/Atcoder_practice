n = int(input())

i = 2
x = 2
cnt = 0
ans = []
while i * i <= n:
    while i ** x <= n:
        ans.append(i ** x)
        cnt += 1
        x += 1
    x = 2
    i += 1
print(n - len(set(ans)))


