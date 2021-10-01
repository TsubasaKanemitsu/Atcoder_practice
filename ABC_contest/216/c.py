n = int(input())

ans = ''
while 1 <= n:
    if n % 2 == 1:
        ans += 'A'
        n -= 1
    else:
        ans += 'B'
        n = n // 2
print(ans[::-1])