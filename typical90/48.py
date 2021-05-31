n, k = list(map(int, input().split()))

AB = [list(map(int, input().split())) for _ in range(n)]

AB.sort(key=lambda x:x[1], reverse=True)

num = []
for a, b in AB:
    num.append(a - b)
    num.append(b)
num.sort(reverse=True)

ans = sum(num[0:k])
print(ans)