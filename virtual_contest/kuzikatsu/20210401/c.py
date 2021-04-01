import math
n, m = list(map(int, input().split()))
s = input()
t = input()


def lcm(x, y):
    return (x * y) // math.gcd(x, y)


_lcm = lcm(n, m)

x = [0] * (_lcm + 1)
index1 = []
index2 = []

for i in range(n):
    index = i * int(_lcm / n) + 1
    index1.append(index)
    x[index] = s[i]

for i in range(m):
    index = i * int(_lcm / m) + 1
    index2.append(index)
    x[index] = t[i]

ss = ''
for index in index1:
    ss += x[index]
tt = ''
for index in index2:
    tt += x[index]

print(x, len(x))
if ss == s and tt == t:
    print(_lcm)
else:
    print(-1)
