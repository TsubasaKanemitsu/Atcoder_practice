n = int(input())
X = 0
x = []

for i in range(n):
    a, b = map(int, input().split())
    X-= a
    x.append(a + a + b)

x.sort()
print(x)

ans = 0

while X <= 0:
    X += x.pop()
    ans += 1