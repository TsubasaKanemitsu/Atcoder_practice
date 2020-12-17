x = int(input())
p = 1
num = []
if x == 1:
    num.append(1)
else:
    for b in range(2, 1000):
        p = 2
        while b ** p <= x:
            num.append(b ** p)
            p += 1
ans = max(num)
print(ans)
