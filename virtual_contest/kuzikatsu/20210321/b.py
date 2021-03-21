a, b, c = list(map(int, input().split()))

if a % 2 == 1 or b % 2 == 1 or c % 2 == 1:
    print(0)
    exit()

if a == b == c:
    print(-1)
    exit()

cookie = [a, b, c]
cookie.sort()

a = cookie[0]
b = cookie[1]
c = cookie[2]


cnt = 0
while a % 2 == 0 and b % 2 == 0 and c % 2 == 0:
    half_a = a // 2
    half_b = b // 2
    half_c = c // 2

    a = half_a + half_c
    b = half_b + half_a
    c = half_c + half_b
    cnt += 1
print(cnt)
