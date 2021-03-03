# コーナーケース
n = int(input())

ans = 10 ** 5 + 1

if n == 2:
    print(2)
    exit()
for i in range(2, n - 1):
    a = i
    b = n - a
    a = map(lambda x: int(x), list(str(a)))
    b = map(lambda x: int(x), list(str(b)))
    num = int(sum(a)) + int(sum(b))
    ans = min(ans, num)
print(ans)
